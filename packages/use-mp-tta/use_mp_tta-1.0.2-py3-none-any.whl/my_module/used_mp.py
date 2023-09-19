from boto3.s3.transfer import TransferConfig, S3Transfer
import boto3.session
import os
import re
import struct
import json
import binascii
import datetime
from smart_open import open as op
import logging
import sys

end_point_url = "https://kr.object.gov-ncloudstorage.com"
session = boto3.session.Session(profile_name="tta_2023")
current_directory_path = os.path.dirname(os.path.abspath(__file__))
pattern = r'(\d+-\d+)'
s3_client = session.client("s3", endpoint_url=end_point_url)

# Configure transfer settings
config = TransferConfig(
    multipart_threshold=10 * 1024*1024,
    max_concurrency=10,
    use_threads=True
)

# Create S3Transfer object
transfer = S3Transfer(s3_client, config)

def makeLog():
    match = re.search(pattern, current_directory_path)
    logger = logging.getLogger(match.group(1))
    lgo_level = logging.INFO
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    # add the handler to the logger
    stream_hander = logging.StreamHandler()
    stream_hander.setFormatter(log_format)
    logger.setLevel(lgo_level)
    logger.addHandler(stream_hander)
    # set up lagging to file
    os.makedirs(os.path.join(current_directory_path, "log"), exist_ok=True)
    log_filename = f"{os.path.join(current_directory_path, 'log')}/{datetime.datetime.now().strftime('%Y%m%d')}.log"
    file_handler = logging.FileHandler(log_filename)
    logger.addHandler(file_handler)

    return logger

def s3_bucket_file_download(path, bucket_name):
    global s3_client, transfer

    arr = []
    if os.path.splitext(path)[1] == ".json":
        os.makedirs(
            f"../data/label/{os.path.dirname(path)}", exist_ok=True)
        file_path = os.path.join("../data/label/", path)

        transfer.download_file(bucket_name, path, file_path)
        arr.append(file_path)
    else:
        os.makedirs(
            f"../data/origin/{os.path.dirname(path)}", exist_ok=True)
        file_path = os.path.join("../data/origin/", path)

        transfer.download_file(bucket_name, path, file_path)
        arr.append(file_path)
    return arr


def s3_wavfile_playtime_check(wav_path, bucket_name, error_list=[]):
    global session, end_point_url
    process_pid = os.getpid()
    blocks_2 = [["Subchunk1ID", "B", 4], ["Subchunk1", "L", 4], ["AudioFormat", "L", 2], ["NumChannels", "L", 2], ["SampleRate", "L", 4],
                ["ByteRate", "L", 4], ["BlockAlign", "L", 2], ["BitsPerSample", "L", 2]]
    i = 0
    extra = 0
    play_time = 0
    data_length = 0
    tmp_arr = []  # self로 변수 설정하였더니 중복되는 값이 발생한 거 같음 그래서 함수 시작할 때마다 리셋이 필요한거 같음!!

    # s3_client = session.Session(profile_name="tta")
    s3_resource = session.client(
        service_name="s3", endpoint_url=end_point_url)

    def Little(data):
        if len(data) == 4:
            data = struct.pack("<I", int(binascii.b2a_hex(data), 16))
            return binascii.b2a_hex(data)
        elif len(data) == 2:
            data = struct.pack("<h", int(binascii.b2a_hex(data), 16))
            return binascii.b2a_hex(data)

    def Big(data):
        return binascii.b2a_hex(data)

    def check_s3_bucket_file_size(path):

        response = s3_resource.get_object(
            Bucket=bucket_name, Key=path)
        content_lenght = response["ContentLength"]

        return content_lenght

    def output_duration(length):
        hours = length // 3600
        length %= 3600
        mins = length // 60
        length %= 60
        seconds = round(length, 2)

        return hours, mins, seconds

    with op(f"s3://{bucket_name}/{wav_path}", "rb", transport_params={"client": s3_resource})as wf:
        end_flag = True
        wav_binary_data = wf.readline()

        while end_flag:
            wav_binary_data_2 = wf.readline()

            if b"data" in wav_binary_data:
                wav_binary_data += wav_binary_data_2
                end_flag = False
            else:
                wav_binary_data += wav_binary_data_2

        try:
            i = str(binascii.b2a_hex(wav_binary_data))[2:].index(
                str(binascii.hexlify(b'fmt '))[2:-1]) // 2

        except Exception as e:
            exc_type, exc_obj, exe_tb = sys.exc_info()
            err_lineno = exe_tb.tb_lineno
            mylogger.info("PID:: %s - wav_path:: %s - ERR_MSG:: %s - err_lineno:: %s", process_pid, wav_path, e, err_lineno)
            pass
        for blc in blocks_2:
            # if blc[1] == "B":
            #     print(f"{blc[0]} = {Big(wav_binary_data[i:i+blc[2]])} ({wav_binary_data[i:i+blc[2]]})")
            # if blc[0] == "AudioFormat":
            #     audioFormat = int(Little(wav_binary_data[i:i+blc[2]]), 16)
            if blc[0] == "NumChannels":
                numChannels = int(Little(wav_binary_data[i:i+blc[2]]), 16)
            elif blc[0] == "SampleRate":
                sampleRate = int(Little(wav_binary_data[i:i+blc[2]]), 16)
            elif blc[0] == "BitsPerSample":
                bitsPerSample = int(
                    Little(wav_binary_data[i:i+blc[2]]), 16)
            # else:
            #     print(f"{blc[0]} = {Little(wav_binary_data[i:i+blc[2]])} ({wav_binary_data[i:i+blc[2]]})")
            i += blc[2]

        # extra = str(binascii.b2a_hex(wav_binary_data))[2:].index(str(binascii.hexlify(b'data'))[2:-1]) //2 - i
        # extra_blocks = [["ExtraParmSize", "L", 2], ["ExtraParams", "L", extra - 2]]
        # if extra > 0:
        #     for blc in extra_blocks:
        #         if blc[1] == "B":
        #             print(f"{blc[0]} = {Big(wav_binary_data[i:i+blc[2]])} ({wav_binary_data[i:i+blc[2]]})")
        #         else:
        #             print(f"{blc[0]} = {Little(wav_binary_data[i:i+blc[2]])} ({wav_binary_data[i:i+blc[2]]})")
        #         i += blc[2]
        file_size = check_s3_bucket_file_size(wav_path)
        if numChannels == 1 and bitsPerSample == 8:
            data_length = file_size - 44
            play_time = data_length / sampleRate
        elif numChannels == 1 and bitsPerSample == 16:
            data_length = file_size / 2 - 22
            play_time = data_length / sampleRate
        elif numChannels == 1 and bitsPerSample == 24:
            data_length = file_size / 3 - (44 / 3)
            play_time = data_length / sampleRate
        elif numChannels == 2 and bitsPerSample == 8:
            data_length = file_size / 2 - 22
            play_time = data_length / sampleRate
        elif numChannels == 2 and bitsPerSample == 16:
            data_length = file_size / 4 - 11
            play_time = data_length / sampleRate
        else:
            data_length = file_size / 6 - (44 / 6)
            play_time = data_length / sampleRate
        hours, mins, seconds = output_duration(play_time)
        tmp_arr.append({"file_path": wav_path, "total_play_time": f"{hours}시간 {mins}분 {seconds}초",
                        "origin_seconds": play_time, "fs": sampleRate, "len_data": data_length})
    return tmp_arr


def obj_cnt(path, bucket_name, key, split_begin=4, split_end=4):
    global sessionn, end_point_url

    tmp_list = list()
    s3_client = session.client(service_name="s3", endpoint_url=end_point_url)

    def find_key(data, key):
        if isinstance(data, dict):
            if key in data:
                return data.get(key)
            for k, v in data.items():
                result = obj_cnt(v, key)
                if result is not None:
                    return result
        elif isinstance(data, list):
            for item in data:
                result = obj_cnt(item, key)
                if result is not None:
                    return result
    with op(f"s3://{bucket_name}/{path}", encoding="utf-8-sig", transport_params={"client": s3_client}) as jsonfile:
        json_data = json.load(jsonfile)
        if split_begin == split_end:
            class_name = path.split("/")[split_begin]
        else:
            class_name = "/".join(path.split("/")[split_begin:split_end])
        find_key_result = find_key(json_data, key)
        tmp_list.append({"file_path": path, "class_name": class_name,
                        "obj_cnt": len(find_key_result)})

    return tmp_list

mylogger = makeLog()