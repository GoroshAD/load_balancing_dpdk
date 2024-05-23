from scapy.all import sendp, IP, Ether, UDP, rdpcap
import cmd
import time

class sender(cmd.Cmd):
    """packet sender"""
    prompt = ":"

    def do_rnd_send(self, args):
        sendp(Ether()/IP(dst="170.210.254.4", src="2.2.2.2/24")/UDP(dport=999,sport=666)/f"Hello world!",iface="enp4s0f1", count=int(args))

    def do_fix_send(self, args):
        sendp(Ether()/IP(dst="172.21.253.4")/UDP(dport=999,sport=666)/f"Hello world!",iface="enp4s0f1", count=int(args))

    def do_file_send(self, args):
        file_path, times = args.split()
        times = int(times)
        '''_time = 0
        counter = 0
        with open(file_path, "r") as file:
            lines = file.readlines()
            sending = []
            for line in lines:
                line = line.split(", ")
                tmp_dst, tmp_dst_port = line[1].split()[2].split(":")
                tmp_src, tmp_src_port = line[1].split()[0].split(":")
                tmp_time = float(line[0])*1000000
                if tmp_dst_port == "N/A":
                    tmp_dst_port = 999
                if tmp_src_port == "N/A":
                    tmp_src_port = 666
                sending.append(((tmp_time - _time)/1000000.0, tmp_dst, tmp_src, int(tmp_dst_port), int(tmp_src_port)))
                _time = tmp_time

            for i in sending:
                #time.sleep(i[0])
                
                sendp(Ether()/IP(dst=i[1], src=i[2])/UDP(dport=i[3],sport=i[4])/f"Hello world!", iface="enp4s0f1", verbose=False)
                #print(tmp_time - time, tmp_time)   #, tmp_src, tmp_src_port, tmp_dst, tmp_dst_port)
                counter += 1
                print(counter) if counter % 100 == 0 else None'''
        for i in range(times):
            sendp(rdpcap(file_path),iface="enp4s0f1")

    def do_pretesting(self, args):
        for i in range(1, 201):
            sendp(rdpcap(f"./sender_files/test_{i}.pcap"),iface="enp4s0f1")

    def do_EOF(self, args):
        return True

if __name__ == "__main__":
    sender().cmdloop()


