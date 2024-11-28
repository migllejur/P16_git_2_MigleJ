import logging

logging.basicConfig(level=logging.ERROR,
                    filename="zurnalas.log",
                    encoding="utf-8",
                    format="%(asctime)s || %(levelname)s || %(message)s")

logging.warning("warning lygio žurnalo eilutė")
logging.error("error lygio žurnalo eilutė")
logging.critical("critical lygio žurnalo eilutė")