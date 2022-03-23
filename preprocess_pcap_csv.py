import pandas as pd

#pd.set_option('displ')

pcap_detail_df = pd.read_csv("PortScan_Begin_to_End_tshark_deltail.csv")


pcap_detail_df.info() # 直接查看信息
'''
Data columns (total 39 columns):
 #   Column               Dtype  
---  ------               -----  
 0   ip.version           float64
 1   ip.hdr_len           float64
 2   ip.tos               float64
 3   ip.id                object 
 4   ip.flags             object 
 5   ip.flags.rb          float64
 6   ip.flags.df          float64
 7   ip.flags.mf          float64
 8   ip.frag_offset       float64
 9   ip.ttl               float64
 10  ip.proto             float64
 11  ip.checksum          object 
 12  ip.src               object 
 13  ip.dst               object 
 14  ip.len               float64
 15  ip.dsfield           object 
 16  tcp.srcport          float64
 17  tcp.dstport          float64
 18  tcp.seq              float64
 19  tcp.ack              float64
 20  tcp.len              float64
 21  tcp.hdr_len          float64
 22  tcp.flags            object 
 23  tcp.flags.fin        float64
 24  tcp.flags.syn        float64
 25  tcp.flags.reset      float64
 26  tcp.flags.push       float64
 27  tcp.flags.ack        float64
 28  tcp.flags.urg        float64
 29  tcp.flags.cwr        float64
 30  tcp.window_size      float64
 31  tcp.checksum         object 
 32  tcp.urgent_pointer   float64
 33  tcp.options.mss_val  float64
 34  frame.time_delta     float64
 35  tcp.stream           float64
 36  frame.time_relative  float64
 37  tcp.time_delta       float64
 38  tcp.time_relative    float64
dtypes: float64(31), object(8)
memory usage: 561.0+ MB
'''
print(pcap_detail_df.isnull().sum()) # 每列有多少个缺失值
'''
memory usage: 561.0+ MB
ip.version               14792
ip.hdr_len               21690
ip.tos                 1885472
ip.id                    21690
ip.flags                 21690
ip.flags.rb              21690
ip.flags.df              21690
ip.flags.mf              21690
ip.frag_offset           21690
ip.ttl                   21690
ip.proto                 21690
ip.checksum              21690
ip.src                   21690
ip.dst                   21690
ip.len                   21690
ip.dsfield               21690
tcp.srcport             234853
tcp.dstport             234853
tcp.seq                 234853
tcp.ack                 234859
tcp.len                 234989
tcp.hdr_len             234859
tcp.flags               234859
tcp.flags.fin           234859
tcp.flags.syn           234859
tcp.flags.reset         234859
tcp.flags.push          234859
tcp.flags.ack           234859
tcp.flags.urg           234859
tcp.flags.cwr           234859
tcp.window_size         234859
tcp.checksum            234859
tcp.urgent_pointer      234859
tcp.options.mss_val    1663957
frame.time_delta             0
tcp.stream              234859
frame.time_relative          0
tcp.time_delta          234859
tcp.time_relative       234859
'''
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

# add label
pcap_detail_df["label"] = pcap_detail_df.apply(lambda x: 1 if x["ip.src"] == "172.16.0.1" else 0, axis=1)

print(pcap_detail_df.groupby('label').size())

print(pcap_detail_df.head(5))

pcap_detail_df.to_csv("PortScan_Begin_to_End_tshark_deltail_with_label.csv", index=False)

