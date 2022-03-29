import pandas as pd

#pd.set_option('displ')
for i in range(4, 6 + 1):

    csv_name = "sample" + str(i) + ".csv"
    pcap_detail_df = pd.read_csv(csv_name)


    pcap_detail_df.info() # 直接查看信息
    print(pcap_detail_df.isnull().sum()) # 每列有多少个缺失值

    print(pcap_detail_df.isna().sum(1)) # 每行有多少个缺失值





    # drop totally duplicated rows
    pcap_detail_df = pcap_detail_df.drop_duplicates()


    # drop the rows contains Nan
    pcap_detail_df = pcap_detail_df.dropna(axis = 0, subset = ["ip.src"])
    pcap_detail_df = pcap_detail_df.dropna(axis = 0, subset = ["tcp.window_size"])


    # drop ip.tos, which are all Nan
    pcap_detail_df = pcap_detail_df.drop(columns=["ip.tos"])

    # delete the quote of elements
    def delete_quote(x: str):
        return x.strip("") if x is str else x
    pcap_detail_df = pcap_detail_df.applymap(delete_quote)


    # fill Nan wiith 0
    pcap_detail_df.fillna(0, inplace=True)

    # change hexadecimal number to decimal number
    hexadecimal_columns = ["ip.id", "ip.checksum", "ip.dsfield", "tcp.flags", "tcp.checksum"]
    def hexadecimal_to_decimal(x: str):
        if "0x" in str(x):
            return int(str(x), 16)
        return x
    pcap_detail_df = pcap_detail_df.applymap(hexadecimal_to_decimal)
    '''
    # add label
    pcap_detail_df["label"] = pcap_detail_df.apply(lambda x: 1 if x["ip.src"] == "172.16.0.1" else 0, axis=1)

    print(pcap_detail_df.groupby('label').size())

    print(pcap_detail_df.head(5))
    '''
    pcap_detail_df.to_csv("after_preprocess_"+ csv_name, index=False)

