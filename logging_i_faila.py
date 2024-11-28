import logging

logging.basicConfig(level=logging.ERROR,
                    filename="zurnalas.log",
                    encoding="utf-8",
                    format="%(asctime)s || %(levelname)s || %(message)s")

logging.debug("debug lygio žurnalo eilutė")  # nebus printinama
logging.info("info lygio žurnalo eilutė")  # nebus printinama
logging.warning("warning lygio žurnalo eilutė")
logging.error("error lygio žurnalo eilutė")
logging.critical("critical lygio žurnalo eilutė")