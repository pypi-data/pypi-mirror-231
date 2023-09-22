import logging

from asyncfix import FTag
from asyncfix.message import MessageDirection


class FIXSession:
    def __init__(self, key, target_comp_id, sender_comp_id):
        self.key = key
        self.sender_comp_id = sender_comp_id
        self.target_comp_id = target_comp_id

        self.snd_seq_num = None
        self.messages = None
        self.next_expected_msg_seq_num = None

        self.reset_msgs()

    def reset_msgs(self):
        self.snd_seq_num = 0
        self.next_expected_msg_seq_num = 1
        self.messages = {MessageDirection.OUTBOUND: {}, MessageDirection.INBOUND: {}}

    def validate_comp_ids(self, target_comp_id, sender_comp_id):
        return (
            self.sender_comp_id == sender_comp_id
            and self.target_comp_id == target_comp_id
        )

    def allocate_snd_seq_no(self):
        self.snd_seq_num += 1
        return str(self.snd_seq_num)

    def validate_recv_seq_no(self, seq_no):
        if self.next_expected_msg_seq_num < int(seq_no):
            logging.warning(
                "SeqNum from client unexpected (Rcvd: %s Expected: %s)"
                % (seq_no, self.next_expected_msg_seq_num)
            )
            return (False, self.next_expected_msg_seq_num)
        else:
            return (True, seq_no)

    def reset_seq_num(self):
        self.snd_seq_num = 0
        self.next_expected_msg_seq_num = 1

    def set_recv_seq_no(self, seq_no):
        # if self.nextExpectedMsgSeqNum != int(seqNo):
        #     logging.warning("SeqNum from client unexpected (Rcvd: %s Expected: %s)"
        #           % (seqNo, self.nextExpectedMsgSeqNum))
        self.next_expected_msg_seq_num = int(seq_no) + 1

    def persist_msg(self, msg, direction):
        seqNo = msg[FTag.MsgSeqNum]
        self.messages[direction][seqNo] = msg
