import requests
import csv
import time
import logging
from datetime import datetime

from line import Line

logger = logging.getLogger(__name__)
url = "http://app.metrolisboa.pt/status/getLinhas.php"
file_path = "data.csv"

wait_in_minutes = 1
wait_in_seconds = wait_in_minutes * 60


def create_line_objects(response, time_stamp):
    lines = []
    amarela = Line("amarela", response["amarela"],
                   response["tipo_msg_am"], time_stamp)
    lines.append(amarela)

    azul = Line("azul", response["azul"],
                response["tipo_msg_az"], time_stamp)
    lines.append(azul)

    vermelha = Line("vermelha", response["vermelha"],
                    response["tipo_msg_vm"], time_stamp)
    lines.append(vermelha)

    verde = Line("verde", response["verde"],
                 response["tipo_msg_vd"], time_stamp)
    lines.append(verde)

    return lines


def download():
    res = requests.get(url)

    if res.status_code == 200:
        content = res.json()
        content = content["resposta"]

        lines = create_line_objects(content, datetime.now())

        with open(file_path, "a") as f:
            writer = csv.writer(f)

            for line in lines:
                writer.writerow(line.to_csv())
            logger.info("Saving {} lines to file".format(len(lines)))
    else:
        logger.info("Request returned error {}".format(res.status_code))


if __name__ == "__main__":
    logger.info("Operation started")
    download()

    logger.info("Operation finished")
