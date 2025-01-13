import cianparser

moscow_parser = cianparser.CianParser(location="Санкт-Петербург")
data = moscow_parser.get_flats(
    deal_type="sale", rooms=(4), with_saving_csv=True)
