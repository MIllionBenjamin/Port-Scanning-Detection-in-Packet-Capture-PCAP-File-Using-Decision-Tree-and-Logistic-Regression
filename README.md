For the report, please visit the [report.docx](https://github.com/MIllionBenjamin/Port-Scanning-Detection-in-Packet-Capture-PCAP-File-Using-Decision-Tree-and-Logistic-Regression/blob/main/report.docx) in this repo.

```shell
tshark -r PortScan_Begin_to_End.pcap -T fields -E header=y -E separator=, -E quote=d -E occurrence=f -e ip.version -e ip.hdr_len -e ip.tos -e ip.id -e ip.flags -e ip.flags.rb -e ip.flags.df -e ip.flags.mf -e ip.frag_offset -e ip.ttl -e ip.proto -e ip.checksum -e ip.src -e ip.dst -e ip.len -e ip.dsfield -e tcp.srcport -e tcp.dstport -e tcp.seq -e tcp.ack -e tcp.len -e tcp.hdr_len -e tcp.flags -e tcp.flags.fin -e tcp.flags.syn -e tcp.flags.reset -e tcp.flags.push -e tcp.flags.ack -e tcp.flags.urg -e tcp.flags.cwr -e tcp.window_size -e tcp.checksum -e tcp.urgent_pointer -e tcp.options.mss_val -e frame.time_delta -e tcp.stream -e frame.time_relative -e tcp.time_delta -e tcp.time_relative > PortScan_Begin_to_End_tshark_deltail.csv
```
