import logging

logging.basicConfig(level=logging.INFO,
                    filename="aritmetika.log",
                    encoding="utf-8",
                    format="%(asctime)s || %(levelname)s || %(message)s")

logging.info("Kviečiama kaupk_aritmetika funkcija")


def kaupk_aritmetika(*args, operacija="suma"):
    if len(args) < 2:
        logging.info(f"Panaudoti argumentai: {args}")
        logging.error("Įrašytas nepakankamas duomenų skaičius")
        return args
    if operacija == "daugyba":
        logging.info(f"Panaudoti argumentai: {args}")
        logging.info("Pasirinkta daugybos operacija")
        rezultatas = 1
        for nr in args:
            rezultatas *= nr
    elif operacija == "dalyba":
        logging.info(f"Panaudoti argumentai: {args}")
        logging.info("Pasirinkta dalybos operacija")
        rezultatas = args[0]
        for nr in args[1:]:
            if nr == 0:
                logging.warning("Dalyba iš nulio negalima")
                return False
            rezultatas /= nr
    elif operacija == "suma":
        logging.info(f"Panaudoti argumentai: {args}")
        logging.info("Pasirinkta default (sumos) operacija")
        rezultatas = sum(args)
    elif operacija == "atimtis":
        logging.info(f"Panaudoti argumentai: {args}")
        logging.info("Pasirinkta atimties operacija")
        rezultatas = args[0]
        for nr in args[1:]:
            rezultatas -= nr
    else:
        logging.error(f"Nežinoma operacija: {operacija}")
        return None
    logging.info(f"Grąžinamas rezultatas: {rezultatas}")
    return rezultatas