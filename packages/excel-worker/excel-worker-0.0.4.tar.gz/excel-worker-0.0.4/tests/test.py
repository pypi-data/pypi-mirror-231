from excel_worker import Excel
from excel_worker.types import BeautifulType

ex = Excel()
ex.setup('main', {'main': []})
ex.add_key_value('main', '123')
ex.add_key_value('main', '2')
ex.add_key_value('main2', '2')
path = ex.write_excel('test.xlsx', beautiful_type=BeautifulType.no_beautiful)
print(path)
