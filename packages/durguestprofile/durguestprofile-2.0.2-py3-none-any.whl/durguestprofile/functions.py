from scipy.sparse import csr_matrix
import sparse_dot_topn.sparse_dot_topn as ct
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import pandas as pd
import numpy as np
import datetime as dt
import os
from glob import glob
import xml.etree.ElementTree as ET
try:
    from .utilities import json_normalize
    from .xmltodict import parse
except:
    from durguestprofile.utilities import json_normalize
    from durguestprofile.xmltodict import parse

# user define functions
# -----------------------------

def isnan(value: str) -> bool:
    """
    check if the value is NoneType
    @param value:
    @rtype: str
    @return: bool
    """
    import math
    try:
        return math.isnan(float(value))
    except:
        return False


def check_if_email_address(email_address: str) -> bool:
    """
    Chech if the string is real email address, using REGX patterns

    Parameters
    ----------
        email_address

    Returns
    -------
        return: bool

    Examples
    --------
    >>> check_if_email_address("support@roinsight.com")
    True
    >>> check_if_email_address("support@roinsight")
    False

    """
    try:
        if email_address is not None and not isnan(email_address):
            if email_address[email_address.find('@')+1:].lower() == 'guest.booking.com':
                return True
            if re.match("[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-z]{1,3}", str(email_address).lower()):
                return False
            else:
                return True
        else:
            return True
    except:
        email_address


def match_adddress(country_cd, adr_state, adr_city, adr_zip_code, adr_street_name):
    """
    United States: US
    United Kingdom: GB
    Canada: CA
    Australia: AU
    France: FR
    Germany: DE
    Italy: IT
    Spain: ES
    China: CN
    Japan: JP

    :param country_cd:
    :param adr_state:
    :param adr_city:
    :param adr_zip_code:
    :param adr_street_name:
    :return:
    """
    from i18naddress import InvalidAddress, normalize_address

    error = 'not_validated'
    if country_cd in ['US', 'GB', 'CA', 'AU', 'FR', 'DE', 'IT', 'ES', 'CN', 'JP']:
        try:
            address = normalize_address({
                'country_code': '' if isnan(country_cd) else country_cd,
                'country_area': '' if isnan(adr_state) else adr_state,
                'city': '' if isnan(adr_city) else adr_city,
                'postal_code': '' if isnan(adr_zip_code) else adr_zip_code,
                'street_address': '' if isnan(adr_street_name) else adr_street_name
            })
            error = 'valid'
        except InvalidAddress as e:
            error = e.errors

    # Validate default input
    # elif country_cd in ['SA']:

    else:
        address = {
            # 'country_code': '' if isnan(country_cd) else country_cd,
            # 'country_area': True if isnan(adr_state) else adr_state,
            'city': 'required' if isnan(adr_city) else adr_city,
            # 'postal_code': True if isnan(adr_zip_code) else adr_zip_code,
            'street_address': 'required' if isnan(adr_street_name) else adr_street_name
        }
        if any([True for v in address.values() if v == 'required']):
            error = address
        # error = 'not_validated'

    return error


def validate_address(address):
    if not isnan(address):
        if str(address).lower().__contains__('xx'):
            return True
        else:
            return False
    else:
        return False


def validate_phone_number(telephone):

    import phonenumbers
    tel = re.findall(r'\b\d+\b', telephone)
    if len(tel) > 0 and telephone not in ['0', 0]:
        phone = ''.join(tel)
        # Remove trailing zeros
        if phone.startswith('0'):
            phone = re.sub("^0+(?!$)", "", phone)
        try:
            is_phone = phonenumbers.is_possible_number(phonenumbers.parse("+" + phone))
        except Exception as e:
            is_phone = False

    # elif len(tel) == 0:
    #     is_phone = phonenumbers.is_possible_number(phonenumbers.parse(telephone))

    else:
        is_phone = False

    return is_phone


def ngrams(string, n=3):
    # pad names for ngrams...
    string = ' ' + string + ' '
    string = re.sub(r'[,-./]|\sBD', r'', string)
    ngrams = zip(*[string[i:] for i in range(n)])
    return [''.join(ngram) for ngram in ngrams]


def awesome_cossim_top(a, b, ntop, lower_bound=0.0):
    # force A and B as a CSR matrix.
    # If they have already been CSR, there is no overhead
    a = a.tocsr()
    b = b.tocsr()
    m, _ = a.shape
    _, n = b.shape

    idx_dtype = np.int32
    nnz_max = m * ntop
    indptr = np.zeros(m + 1, dtype=idx_dtype)
    indices = np.zeros(nnz_max, dtype=idx_dtype)
    data = np.zeros(nnz_max, dtype=a.dtype)

    ct.sparse_dot_topn(
        m, n, np.asarray(a.indptr, dtype=idx_dtype),
        np.asarray(a.indices, dtype=idx_dtype),
        a.data,
        np.asarray(b.indptr, dtype=idx_dtype),
        np.asarray(b.indices, dtype=idx_dtype),
        b.data,
        ntop,
        lower_bound,
        indptr, indices, data)

    return csr_matrix((data, indices, indptr), shape=(m, n))


def get_matches_df(sparse_matrix, name_vector, top=100):
    non_zeros = sparse_matrix.nonzero()
    sparserows = non_zeros[0]
    sparsecols = non_zeros[1]
    if top:
        nr_matches = top
    else:
        nr_matches = sparsecols.size

    left_side = np.empty([nr_matches], dtype=object)
    right_side = np.empty([nr_matches], dtype=object)
    similairity = np.zeros(nr_matches)

    for index in range(0, nr_matches):
        left_side[index] = name_vector[sparserows[index]]
        right_side[index] = name_vector[sparsecols[index]]
        similairity[index] = sparse_matrix.data[index]

    return pd.DataFrame({'merge_with_full_name': left_side,
                         'full_name': right_side,
                         'similarity': similairity})


def find_non_merged_profiles(dframe):

    main_matches = dframe.copy()
    main_matches["full_name"] = main_matches['first_name'] + " " + main_matches["last_name"]
    main_matches = main_matches[['hotel_code','full_name', 'guest_name_id']].copy()
    main_matches.drop_duplicates(inplace=True)
    main_matches.dropna(inplace=True)

    osr_matches_duplicated = main_matches.loc[main_matches[['hotel_code', 'full_name']].duplicated()].copy()
    osr_matches_duplicated.rename(columns={'full_name': 'merge_with_full_name'}, inplace=True)
    osr_matches_duplicated['similarity'] = 1

    dframes_matched = []
    for hotel_code in main_matches['hotel_code'].unique():
        osr_matches = main_matches.loc[main_matches['hotel_code'] == hotel_code].copy()

        guest_names = np.asarray(osr_matches['full_name'].unique(), dtype=object)
        vectorizer = TfidfVectorizer(min_df=1, analyzer=ngrams)
        tf_idf_matrix = vectorizer.fit_transform(guest_names)
        matches = awesome_cossim_top(tf_idf_matrix, tf_idf_matrix.transpose(), 10, .70)
        matches_df = get_matches_df(matches, guest_names, top=matches.nonzero()[1].size)

        # Remove all exact matches
        matches_df = matches_df[matches_df['similarity'] < 0.99999].copy()

        # remove family name matches
        matches_df = matches_df[matches_df['similarity'] > 0.80].copy()
        matches_df.sort_values(['similarity'], ascending=False, inplace=True)

        matches_df = matches_df[['full_name', 'similarity', 'merge_with_full_name']].copy()

        matches_df = pd.merge(osr_matches, matches_df, how='left', on='full_name')
        matches_df.dropna(subset=['similarity'], inplace=True)
        matches_df = matches_df[['guest_name_id', 'similarity', 'merge_with_full_name']].copy()
        matches_df['hotel_code'] = hotel_code
        dframes_matched.append(matches_df)

    final_matches_df = pd.concat(dframes_matched)

    final_df = pd.concat([final_matches_df, osr_matches_duplicated])
    final_df.drop_duplicates(subset=['hotel_code','guest_name_id'], inplace=True)

    return final_df


def parse_clean_file(file):

    column_names = [
        'hotel_code',
        'external_reference',
        'confirmation_number',
        'status',
        'arrival_date',
        'departure_date',
        'guest_name_id',
        'first_name',
        'last_name',
        'title',
        'country_cd',
        'country_name',
        'language_code',
        'address_type',
        'adr_street_name',
        'adr_additional',
        'adr_additonal_1',
        'adr_additional_2',
        'adr_state',
        'adr_state_name',
        'adr_zip_code',
        'adr_city',
        'telephone',
        'telephone_type',
        'multiple_phones_yn',
        'email_address',
        'nationality_code',
        'nationality_description',
        'multiple_address_yn',
        'creation_date',
        'insert_user',
        'last_update_date',
        'last_update_user',
    ]

    if file.lower().endswith('txt'):
        with open(file, encoding="utf8") as f:
            contents = f.readlines()

        contents = contents[2:-2]

        with open(file + ".csv", encoding="utf8", mode="w") as f:
            for line in contents:
                f.write(line)

                for delimiter in ['|', ',', '\t']:
                    if line.__contains__(delimiter) and len(line.split(delimiter)) > 15:
                        sep = delimiter

        dframe = pd.read_csv(file + ".csv", sep=sep, engine='python', on_bad_lines='skip', dtype=str)
        dframe.columns = column_names


    if file.lower().endswith('xml'):
        xmlstr = ET.tostring(ET.parse(file).getroot(), encoding='utf-8', method='xml')
        data_dict = dict(parse(xmlstr))
        if "OSR_LANDSCAPE" in data_dict.keys():
            required_columns = data_dict["OSR_LANDSCAPE"]["LIST_G_C6"]["G_C6"]
            dframe = pd.json_normalize(json_normalize(required_columns))
            dframe.columns = column_names
        else:
            dframe = pd.DataFrame(dict(zip(column_names, [np.NaN for _ in range(len(column_names))])), index=[0])

    # Update dates
    for col in dframe.columns:
        if col.lower().endswith('date'):
            # dframe[col] = pd.to_datetime(dframe[col], format='mixed')
            dframe[col] = dframe[col]


    return dframe


def final_scoring(dframe, criteria_file=None):

    # define the guest profile data
    criteria_main = {
        "guest_name_id": 15,
        "title": 5,
        "country_cd": 5,
        "adr_street_name": 10,
        "adr_city": 10,
        "telephone": 10,
        "email_address": 10,
        "nationality_code": 15,

        # additional criterias
        "language_code": 3,
        "adr_additional": 3,
        "adr_additonal_1": 2,
        "adr_additional_2": 2,
        "adr_state": 4,
        "adr_zip_code": 4,
        "telephone_type": 2,
    }
    criteria_grouping = {}
    # define the audit criteria and their weights
    if criteria_file is None:
        criteria = criteria_main

    else:
        if os.path.exists(criteria_file):
            criteria_df = pd.read_excel(criteria_file)
            criteria_cleaned = criteria_df.dropna(subset=['CRITERIA'])
            criteria = dict(zip(criteria_cleaned['COLUMN_NAME'].str.lower(), criteria_cleaned['CRITERIA']))
            scoring_cleaned = criteria_df[['SCORING', 'SCORING_CRITERIA']].copy().dropna()
            scoring = dict(zip(scoring_cleaned['SCORING'], scoring_cleaned['SCORING_CRITERIA']))
            criteria_grouping = criteria_cleaned[
                ['GROUPING', 'COLUMN_NAME']].groupby('GROUPING')['COLUMN_NAME'].apply(list).to_dict()
        else:
            print(f"criteria_mapper.xlsx does not exist in {os.getcwd()}")
            criteria = criteria_main
            print("the following criteria will be used.", criteria)
            # raise FileExistsError("criteria_mapper.xlsx")

    matches_df = find_non_merged_profiles(dframe)
    dframe = dframe.merge(matches_df, how='left', on=['guest_name_id', 'hotel_code'])
    dframe.loc[~dframe['similarity'].isna(), "guest_name_id_score"] = 0
    dframe["guest_name_id_score"].fillna(criteria["guest_name_id"], inplace=True)

    # initialize the scores for each criterion
    for col in criteria.keys():
        if col.startswith(('adr_street_name', 'adr_additional')):
            dframe.loc[dframe[col].apply(lambda x: validate_address(x)), col + "_score"] = 0

        if col == 'email_address':
            dframe.loc[dframe[col].apply(lambda x: check_if_email_address(x)), col + "_score"] = 0

        if col == 'adr_zip_code':
            # break
            dframe['is_address_valid'] = dframe[['country_cd', 'adr_state', 'adr_city', 'adr_zip_code', 'adr_street_name']].apply(
                lambda x: match_adddress(x['country_cd'], x['adr_state'], x['adr_city'], x['adr_zip_code'],
                                         x['adr_street_name']), axis=1)
            for col_score in ['country_cd', 'adr_state', 'adr_city', 'adr_zip_code', 'adr_street_name']:
                dframe.loc[~dframe['is_address_valid'].isin(['not_validated', 'valid']), col_score + "_score"] = 0

        if col == 'telephone':
            # dframe['is_phone_number_valid'] = dframe[col].apply(lambda x: validate_phone_number(x))
            dframe.loc[~dframe[col].apply(lambda x: validate_phone_number(str(x))), col + "_score"] = 0

        dframe.loc[dframe[col].isna(), col+"_score"] = 0
        dframe[col + "_score"].fillna(criteria[col], inplace=True)

    # evaluate each criterion and assign a score to grouping
    for k, v in criteria_grouping.items():
        dframe[k.lower() + '_score'] = dframe[[z.lower() + '_score' for z in v]].sum(axis=1, numeric_only=True)

    # calculate the weighted average score
    score_columns = [col+"_score" for col in criteria.keys()]
    dframe['overall_score'] = dframe[score_columns].sum(axis=1, numeric_only=True)

    dframe['base_score'] = 100
    dframe['booking_count'] = 1

    return dframe


def properties_score(files_folder=None,  criteria_file=None):

    if files_folder is None:
        import tkinter
        from tkinter import filedialog
        root = tkinter.Tk()

        files_folder = filedialog.askdirectory(
            title="Select Folder that contains Guest Profile Audit files.")
        root.destroy()

    # The tuple of file types should be either XML or TXT.
    files_list = []
    for extension in ('*.txt', '*.xml'):
        files_list.extend(glob(os.path.join(files_folder, extension)))

    # get the last dates
    _dates_list = [''.join(re.findall(r'[\d]+', os.path.basename(i))) for i in files_list]
    dates_list = []
    date_format = '%d%m%Y%H%M%S%f'
    for indx, i in enumerate(_dates_list):
        try:
            dates_list.append(dt.datetime.strptime(i, date_format).date())
        except Exception as ex:
            dates_list.append(dt.datetime.strptime('0409202349147661', date_format).date())
            print(F'The following file does not contains datetime stamp {files_list[indx]}')

    # dates_list = [dt.datetime.strptime(i, '%d%m%y') for i in _dates_list]
    get_max_date = max(dates_list)
    define_path = [True if i == get_max_date else False for i in dates_list]
    files_list_new = list({key: val for key, val in dict(zip(files_list, define_path)).items() if val}.keys())

    dframes_list = []
    for file in files_list_new:
        print(f'Parsing {file}')
        dframe = parse_clean_file(file)
        dframe['file_name'] = os.path.split(file)[1]
        dframes_list.append(dframe)

    dframe = pd.concat(dframes_list)

    dframe.dropna(subset=['hotel_code'], inplace=True)

    dframe.drop_duplicates(subset=[
        'hotel_code', 'external_reference', 'confirmation_number', 'arrival_date', 'departure_date'
    ], inplace=True)

    dframe['max_file_date'] = get_max_date

    # call the audit function and print the final score
    df = final_scoring(dframe, criteria_file)

    # Change columns name to title case
    df.columns = [col.replace('_', ' ').title() for col in df.columns]

    # save the final dataframe into same folder
    name_of_file = 'FINAL_AUDIT_DATE'

    # df.to_csv(file_name)
    try:
        file_name = os.path.join(files_folder, f'{name_of_file}.csv')
        df.to_csv(file_name, index=False, encoding='utf-8-sig')
    except PermissionError as ex:
        file_name = os.path.join(files_folder, f'{name_of_file}_{dt.datetime.now().strftime("%Y%m%d%H%M%S")}.csv')
        df.to_csv(file_name, index=False, encoding='utf-8-sig')

    print(file_name, 'has been generated.')

    return df

