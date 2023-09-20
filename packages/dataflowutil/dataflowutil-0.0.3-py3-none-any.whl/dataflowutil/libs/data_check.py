import pandas as pd
import warnings
import Levenshtein

def jaccard_index(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return (intersection / union)

def corr_compare_number(value1, value2, tolerance=1e-6):
    return abs(value1 - value2) < tolerance

def check_types_columns(data_bucket,data_local):
    var_levenshtein = 1 - Levenshtein.distance(data_bucket.dtypes.values, data_local.dtypes.values) / max(len(data_bucket.dtypes.values), len(data_local.dtypes.values))
    print(f"** Error Types Columns: {var_levenshtein}")
    print("")
    check_types = pd.DataFrame({"columns_data_bucket":tuple(data_bucket.dtypes.values),"columns_data_local":tuple(data_local.dtypes.values)})
    print(check_types)

def check_count_columns(data_bucket,data_local):
    count = 1 - abs(len(data_bucket.columns) - len(data_local.columns)) / max(len(data_bucket.columns) , len(data_local.columns))
    print(f"** Different Count Columns ({len(data_bucket.columns)}/{len(data_local.columns)}) : {count} ")
    print("")

    list_columns_bucket = data_bucket.columns
    list_columns_local = data_local.columns
    
    data_check_test = pd.DataFrame([list_columns_bucket,list_columns_local]).T
    
    data_check_test.rename(columns = {0:"columns_data_bucket",1:"columns_data_local"}, inplace = True)

    if len(data_local.columns) == len(data_bucket.columns):
        
        list_columns_bucket = data_bucket.columns
        list_columns_local = data_local.columns

        data_check_test["levenshtein_name_columns"] = data_check_test.apply(lambda row: 1 - Levenshtein.distance(row["columns_data_bucket"], row["columns_data_local"]) / max(len(row["columns_data_bucket"]), len(row["columns_data_local"])), axis=1)

    print(data_check_test)

def dft_rows(data_bucket,data_local,column_check):
    merged_df = pd.merge(data_local[f"{column_check}"], data_bucket[f"{column_check}"], left_index=True, right_index=True, suffixes=('_local', '_bucket'))
    different_rows = merged_df[merged_df[f'{column_check}_local'] != merged_df[f'{column_check}_bucket']]
    return different_rows


def check_porcent_value_numeric(key,data_bucket,data_local):
    total = data_bucket[key].ne(data_local[key]).count()
    try:
        check_true = data_bucket[key].ne(data_local[key]).value_counts()[True]
        return f"{100 - abs(check_true / total)}"
    except:
        return f"{100}"


def corr(data_bucket,data_local):
    warnings.simplefilter(action='ignore', category=FutureWarning)        

    check_columns_data_bucket = data_bucket.select_dtypes(include=['object','string'])

    if len(check_columns_data_bucket.columns) > 0:

        print("")
        print("************************************")
        print("*** Corr DTypes Objects/Strings ***")
        print("************************************")
        print("")

        for a in check_columns_data_bucket.columns:
            data_bucket_corr = data_bucket[[a]].astype("category")[a].cat.codes
            data_local_corr = data_local[[a]].astype("category")[a].cat.codes

            var_jaccard = jaccard_index(set(data_bucket_corr), set(data_local_corr))
            var_levenshtein = 1 - Levenshtein.distance(data_bucket[a], data_local[a]) / max(len(data_bucket[a]), len(data_local[a]))

            print(f"{a.ljust(16)} {var_jaccard} - {var_levenshtein}")

    print("")
    print("************************************")
    print("******* Corr DTypes Numbers *******")
    print("************************************")
    print("")
    correlation = data_bucket.corrwith(data_local,method=corr_compare_number)
    for a in correlation.keys():
        value =  sum(correlation[a]) / len(correlation[a])
        print(f"{a.ljust(16)} {value} - {check_porcent_value_numeric(a,data_bucket,data_local)}")
    #return correlation
