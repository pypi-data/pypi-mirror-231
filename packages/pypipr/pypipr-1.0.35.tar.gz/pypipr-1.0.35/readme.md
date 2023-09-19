
# About
The Python Package Index Project (pypipr)

pypi : https://pypi.org/project/pypipr


# Setup
Install with pip
```
pip install pypipr
```

Import with * for fastest access
```python
from pypipr.pypipr import *
```

# CONSTANT

`LINUX`

`WINDOWS`

# FUNCTION

## avg

`avg(i)`

Simple Average Function karena tidak disediakan oleh python  

```python  
n = [1, 22, 2, 3, 13, 2, 123, 12, 31, 2, 2, 12, 2, 1]  
print(avg(n))  
```

Output:
```py
16.285714285714285
```

## basename

`basename(path)`

Mengembalikan nama file dari path  

```python  
print(basename("/ini/nama/folder/ke/file.py"))  
```

Output:
```py
file.py
```

## batch_calculate

`batch_calculate(pattern)`

Analisa perhitungan massal.  
Bisa digunakan untuk mencari alternatif terendah/tertinggi/dsb.  


```python  
iprint(batch_calculate("{1 10} m ** {1 3}"))  
```

Output:
```py
[('1 m ** 1', <Quantity(1, 'meter')>),
 ('1 m ** 2', <Quantity(1, 'meter ** 2')>),
 ('1 m ** 3', <Quantity(1, 'meter ** 3')>),
 ('2 m ** 1', <Quantity(2, 'meter')>),
 ('2 m ** 2', <Quantity(2, 'meter ** 2')>),
 ('2 m ** 3', <Quantity(2, 'meter ** 3')>),
 ('3 m ** 1', <Quantity(3, 'meter')>),
 ('3 m ** 2', <Quantity(3, 'meter ** 2')>),
 ('3 m ** 3', <Quantity(3, 'meter ** 3')>),
 ('4 m ** 1', <Quantity(4, 'meter')>),
 ('4 m ** 2', <Quantity(4, 'meter ** 2')>),
 ('4 m ** 3', <Quantity(4, 'meter ** 3')>),
 ('5 m ** 1', <Quantity(5, 'meter')>),
 ('5 m ** 2', <Quantity(5, 'meter ** 2')>),
 ('5 m ** 3', <Quantity(5, 'meter ** 3')>),
 ('6 m ** 1', <Quantity(6, 'meter')>),
 ('6 m ** 2', <Quantity(6, 'meter ** 2')>),
 ('6 m ** 3', <Quantity(6, 'meter ** 3')>),
 ('7 m ** 1', <Quantity(7, 'meter')>),
 ('7 m ** 2', <Quantity(7, 'meter ** 2')>),
 ('7 m ** 3', <Quantity(7, 'meter ** 3')>),
 ('8 m ** 1', <Quantity(8, 'meter')>),
 ('8 m ** 2', <Quantity(8, 'meter ** 2')>),
 ('8 m ** 3', <Quantity(8, 'meter ** 3')>),
 ('9 m ** 1', <Quantity(9, 'meter')>),
 ('9 m ** 2', <Quantity(9, 'meter ** 2')>),
 ('9 m ** 3', <Quantity(9, 'meter ** 3')>),
 ('10 m ** 1', <Quantity(10, 'meter')>),
 ('10 m ** 2', <Quantity(10, 'meter ** 2')>),
 ('10 m ** 3', <Quantity(10, 'meter ** 3')>)]
```

## batchmaker

`batchmaker(pattern: str)`

Alat Bantu untuk membuat teks yang berulang.  
Gunakan `{[start][separator][finish]([separator][step])}`.  
```  
[start] dan [finish]    -> bisa berupa huruf maupun angka  
([separator][step])     -> bersifat optional  
[separator]             -> selain huruf dan angka  
[step]                  -> berupa angka positif  
```  

```python  
s = "Urutan {1/6/3} dan {10:9} dan {j k} dan {Z - A - 15} saja."  
print(batchmaker(s))  
print(list(batchmaker(s)))  
```

Output:
```py
<generator object batchmaker at 0x7762e54dc0>
['Urutan 1 dan 10 dan j dan Z saja.', 'Urutan 1 dan 10 dan j dan K saja.', 'Urutan 1 dan 10 dan k dan Z saja.', 'Urutan 1 dan 10 dan k dan K saja.', 'Urutan 1 dan 9 dan j dan Z saja.', 'Urutan 1 dan 9 dan j dan K saja.', 'Urutan 1 dan 9 dan k dan Z saja.', 'Urutan 1 dan 9 dan k dan K saja.', 'Urutan 4 dan 10 dan j dan Z saja.', 'Urutan 4 dan 10 dan j dan K saja.', 'Urutan 4 dan 10 dan k dan Z saja.', 'Urutan 4 dan 10 dan k dan K saja.', 'Urutan 4 dan 9 dan j dan Z saja.', 'Urutan 4 dan 9 dan j dan K saja.', 'Urutan 4 dan 9 dan k dan Z saja.', 'Urutan 4 dan 9 dan k dan K saja.']
```

## calculate

`calculate(teks)`

Mengembalikan hasil dari perhitungan teks menggunakan modul pint.  
Mendukung perhitungan matematika dasar dengan satuan.  

Return value:  
- Berupa class Quantity dari modul pint  

Format:  
- f"{result:~P}"            -> pretty  
- f"{result:~H}"            -> html  
- result.to_base_units()    -> SI  
- result.to_compact()       -> human readable  

```python  
fx = "3 meter * 10 cm * 3 km"  
res = calculate(fx)  
print(res)  
print(res.to_base_units())  
print(res.to_compact())  
print(f"{res:~P}")  
print(f"{res:~H}")  
```

Output:
```py
90 centimeter * kilometer * meter
900.0 meter ** 3
900.0 meter ** 3
90 cm·km·m
90 cm km m
```

## chunck_array

`chunck_array(array, size, start=0)`

Membagi array menjadi potongan-potongan dengan besaran yg diinginkan  

```python  
array = [2, 3, 12, 3, 3, 42, 42, 1, 43, 2, 42, 41, 4, 24, 32, 42, 3, 12, 32, 42, 42]  
print(chunck_array(array, 5))  
print(list(chunck_array(array, 5)))  
```

Output:
```py
<generator object chunck_array at 0x77625d8a40>
[[2, 3, 12, 3, 3], [42, 42, 1, 43, 2], [42, 41, 4, 24, 32], [42, 3, 12, 32, 42], [42]]
```

## console_run

`console_run(info, command=None, print_info=True, capture_output=False)`

Menjalankan command seperti menjalankan command di Command Terminal  

```py  
console_run('dir')  
console_run('ls')  
```

## create_folder

`create_folder(folder_name)`

Membuat folder.  
Membuat folder secara recursive dengan permission.  

```py  
create_folder("contoh_membuat_folder")  
create_folder("contoh/membuat/folder/recursive")  
create_folder("./contoh_membuat_folder/secara/recursive")  
```

## datetime_from_string

`datetime_from_string(iso_string, timezone='UTC')`

Parse iso_string menjadi datetime object  

```python  
print(datetime_from_string("2022-12-12 15:40:13").isoformat())  
print(datetime_from_string(  
    "2022-12-12 15:40:13",  
    timezone="Asia/Jakarta"  
).isoformat())  
```

Output:
```py
2022-12-12T15:40:13+00:00
2022-12-12T15:40:13+07:00
```

## datetime_now

`datetime_now(timezone=None)`

Memudahkan dalam membuat Datetime untuk suatu timezone tertentu  

```python  
print(datetime_now("Asia/Jakarta"))  
print(datetime_now("GMT"))  
print(datetime_now("Etc/GMT+7"))  
```

Output:
```py
2023-09-18 21:21:44.073703+07:00
2023-09-18 14:21:44.075371+00:00
2023-09-18 07:21:44.078796-07:00
```

## dict_first

`dict_first(d: dict, remove=False)`

Mengambil nilai (key, value) pertama dari dictionary dalam bentuk tuple.  

```python  
d = {  
    "key2": "value2",  
    "key3": "value3",  
    "key1": "value1",  
}  
print(dict_first(d, remove=True))  
print(dict_first(d))  
```

Output:
```py
('key2', 'value2')
('key3', 'value3')
```

## dirname

`dirname(path)`

Mengembalikan nama folder dari path.  
Tanpa trailing slash di akhir.  

```python  
print(dirname("/ini/nama/folder/ke/file.py"))  
```

Output:
```py
/ini/nama/folder/ke
```

## exit_if_empty

`exit_if_empty(*args)`

Keluar dari program apabila seluruh variabel  
setara dengan empty  

```py  
var1 = None  
var2 = '0'  
exit_if_empty(var1, var2)  
```

## filter_empty

`filter_empty(iterable, zero_is_empty=True, str_strip=True)`

Mengembalikan iterabel yang hanya memiliki nilai  

```python  
var = [1, None, False, 0, "0", True, {}, ['eee']]  
print(filter_empty(var))  
```

Output:
```py
<generator object filter_empty at 0x7762e2e7a0>
```

## get_class_method

`get_class_method(cls)`

Mengembalikan berupa tuple yg berisi list dari method dalam class  

```python  
class ExampleGetClassMethod:  
    def a():  
        return [x for x in range(10)]  

    def b():  
        return [x for x in range(10)]  

    def c():  
        return [x for x in range(10)]  

    def d():  
        return [x for x in range(10)]  

print(get_class_method(ExampleGetClassMethod))  
```

Output:
```py
<generator object get_class_method at 0x7762e2e980>
```

## get_filemtime

`get_filemtime(filename)`

Mengambil informasi last modification time file dalam nano seconds  

```python  
print(get_filemtime(__file__))  
```

Output:
```py
1695036972323366696
```

## get_filesize

`get_filesize(filename)`

Mengambil informasi file size dalam bytes  

```python  
print(get_filesize(__file__))  
```

Output:
```py
472
```

## github_pull

`github_pull()`

Menjalankan command `git pull`  

```py  
github_pull()  
```

## github_push

`github_push(commit_msg=None)`

Menjalankan command status, add, commit dan push  

```py  
github_push('Commit Message')  
```

## github_user

`github_user(email=None, name=None)`

Menyimpan email dan nama user secara global sehingga tidak perlu  
menginput nya setiap saat.  

```py  
github_user('my@emil.com', 'MyName')  
```

## idumps

`idumps(data, syntax='yaml', indent=4)`

Mengubah variabel data menjadi string untuk yang dapat dibaca untuk disimpan.  
String yang dihasilkan berbentuk syntax YAML/JSON/HTML.  

```python  
data = {  
    'a': 123,  
    't': ['disini', 'senang', 'disana', 'senang'],  
    'l': (12, 23, [12, 42]),  
}  
print(idumps(data))  
print(idumps(data, syntax='html'))  
```

Output:
```py
a: 123
l: !!python/tuple
- 12
- 23
-   - 12
    - 42
t:
- disini
- senang
- disana
- senang

<table>
    <tbody>
        <tr>
            <th>a</th>
            <td>
                <span>123</span>
            </td>
        </tr>
        <tr>
            <th>t</th>
            <td>
                <ul>
                    <li>
                        <span>disini</span>
                    </li>
                    <li>
                        <span>senang</span>
                    </li>
                    <li>
                        <span>disana</span>
                    </li>
                    <li>
                        <span>senang</span>
                    </li>
                </ul>
            </td>
        </tr>
        <tr>
            <th>l</th>
            <td>
                <ul>
                    <li>
                        <span>12</span>
                    </li>
                    <li>
                        <span>23</span>
                    </li>
                    <li>
                        <ul>
                            <li>
                                <span>12</span>
                            </li>
                            <li>
                                <span>42</span>
                            </li>
                        </ul>
                    </li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

```

## idumps_html

`idumps_html(data, indent=None)`

Serialisasi python variabel menjadi HTML.  
```  
List -> <ul>...</ul>  
Dict -> <table>...</table>  
```  

```python  
data = {  
    'abc': 123,  
    'list': [1, 2, 3, 4, 5],  
    'dict': {'a': 1, 'b':2, 'c':3},  
}  
print(idumps_html(data))  
```

Output:
```py
<table>
  <tbody>
    <tr>
      <th>abc</th>
      <td>
        <span>123</span>
      </td>
    </tr>
    <tr>
      <th>list</th>
      <td>
        <ul>
          <li>
            <span>1</span>
          </li>
          <li>
            <span>2</span>
          </li>
          <li>
            <span>3</span>
          </li>
          <li>
            <span>4</span>
          </li>
          <li>
            <span>5</span>
          </li>
        </ul>
      </td>
    </tr>
    <tr>
      <th>dict</th>
      <td>
        <table>
          <tbody>
            <tr>
              <th>a</th>
              <td>
                <span>1</span>
              </td>
            </tr>
            <tr>
              <th>b</th>
              <td>
                <span>2</span>
              </td>
            </tr>
            <tr>
              <th>c</th>
              <td>
                <span>3</span>
              </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>

```

## iexec

`iexec(python_syntax, import_pypipr=True)`

improve exec() python function untuk mendapatkan outputnya  

```python  
print(iexec('print(9*9)'))  
```

Output:
```py
81

```

## ijoin

`ijoin(iterable, separator='', start='', end='', remove_empty=False, recursive=True, recursive_flat=False, str_strip=False)`

Simplify Python join functions like PHP function.  
Iterable bisa berupa sets, tuple, list, dictionary.  

```python  
arr = {'asd','dfs','weq','qweqw'}  
print(ijoin(arr, ', '))  

arr = '/ini/path/seperti/url/'.split('/')  
print(ijoin(arr, ','))  
print(ijoin(arr, ',', remove_empty=True))  

arr = {'a':'satu', 'b':(12, 34, 56), 'c':'tiga', 'd':'empat'}  
print(ijoin(arr, separator='</li>\n<li>', start='<li>', end='</li>',  
    recursive_flat=True))  
print(ijoin(arr, separator='</div>\n<div>', start='<div>', end='</div>'))  
print(ijoin(10, ' '))  
```

Output:
```py
dfs, qweqw, weq, asd
,ini,path,seperti,url,
ini,path,seperti,url
<li>satu</li>
<li>12</li>
<li>34</li>
<li>56</li>
<li>tiga</li>
<li>empat</li>
<div>satu</div>
<div><div>12</div>
<div>34</div>
<div>56</div></div>
<div>tiga</div>
<div>empat</div>
10
```

## iloads

`iloads(data, syntax='yaml')`

Mengubah string data hasil dari idumps menjadi variabel.  
String data adalah berupa syntax YAML.  

```python  
data = {  
    'a': 123,  
    't': ['disini', 'senang', 'disana', 'senang'],  
    'l': (12, 23, [12, 42])  
}  
s = idumps(data)  
print(iloads(s))  
```

## iloads_html

`iloads_html(html)`

Mengambil data yang berupa list `<ul>`, dan table `<table>` dari html  
dan menjadikannya data python berupa list.  
setiap data yang ditemukan akan dibungkus dengan tuple sebagai separator.  
```  
list (<ul>)     -> list         -> list satu dimensi  
table (<table>) -> list[list]   -> list satu dimensi didalam list  
```  
apabila data berupa ul maka dapat dicek type(data) -> html_ul  
apabila data berupa ol maka dapat dicek type(data) -> html_ol  
apabila data berupa dl maka dapat dicek type(data) -> html_dl  
apabila data berupa table maka dapat dicek type(data) -> html_table  

```python  
pprint.pprint(iloads_html(iopen("https://harga-emas.org/")), depth=10)  
pprint.pprint(iloads_html(iopen("https://harga-emas.org/1-gram/")), depth=10)  
```

Output:
```py
(['Home', 'Emas 1 Gram', 'History', 'Trend', 'Perak 1 Gram', 'Pluang'],
 [['Harga Emas Hari Ini - Senin, 18 September 2023'],
  ['Spot Emas USD↑1.925,96 (+2,18) / oz',
   'Kurs IDR15.140,00 / USD',
   'Emas IDR↑937.485 (+1.061) / gr'],
  ['LM Antam (Jual)1.075.000 / gr', 'LM Antam (Beli)955.000 / gr']],
 [['Harga Emas Hari Ini'],
  ['Gram', 'Gedung Antam Jakarta', 'Pegadaian'],
  ['per Gram (Rp)', 'per Batangan (Rp)', 'per Gram (Rp)', 'per Batangan (Rp)'],
  ['1000',
   '1.016',
   '1.015.600',
   '1.043.040 (+8.200)',
   '1.043.040.000 (+8.200.000)'],
  ['500',
   '2.031',
   '1.015.640',
   '1.043.082 (+8.200)',
   '521.541.000 (+4.100.000)'],
  ['250',
   '4.064',
   '1.016.060',
   '1.043.512 (+8.200)',
   '260.878.000 (+2.050.000)'],
  ['100',
   '10.171',
   '1.017.120',
   '1.044.600 (+8.200)',
   '104.460.000 (+820.000)'],
  ['50', '20.358', '1.017.900', '1.045.400 (+8.200)', '52.270.000 (+410.000)'],
  ['25', '40.779', '1.019.480', '1.047.040 (+8.200)', '26.176.000 (+205.000)'],
  ['10', '102.450', '1.024.500', '1.052.200 (+8.200)', '10.522.000 (+82.000)'],
  ['5', '206.000', '1.030.000', '1.057.800 (+8.200)', '5.289.000 (+41.000)'],
  ['3', '345.556', '1.036.667', '1.064.667 (+8.000)', '3.194.000 (+24.000)'],
  ['2', '522.500', '1.045.000', '1.073.500 (+8.500)', '2.147.000 (+17.000)'],
  ['1', '1.075.000', '1.075.000', '1.104.000 (+8.000)', '1.104.000 (+8.000)'],
  ['0.5', '2.350.000', '1.175.000', '1.208.000 (+8.000)', '604.000 (+4.000)'],
  ['Update harga LM Antam :18 September 2023, pukul 08:05Harga pembelian '
   'kembali :Rp. 955.000/gram',
   'Update harga LM Pegadaian :31 Agustus 2023']],
 [['Spot Harga Emas Hari Ini (Market Open)'],
  ['Satuan', 'USD', 'Kurs\xa0Dollar', 'IDR'],
  ['Ounce\xa0(oz)', '1.925,96 (+2,18)', '15.140,00', '29.159.034'],
  ['Gram\xa0(gr)', '61,92', '15.140,00', '937.485 (+1.061)'],
  ['Kilogram\xa0(kg)', '61.921,05', '15.140,00', '937.484.726'],
  ['Update harga emas :18 September 2023, pukul 21:21Update kurs :13 Febuari '
   '2023, pukul 09:10']],
 [['Gram', 'UBS Gold 99.99%'],
  ['Jual', 'Beli'],
  ['/ Batang', '/ Gram', '/ Batang', '/ Gram'],
  ['100',
   '101.711.300 (+700.000)',
   '1.017.113 (+7.000)',
   '96.085.000 (+450.000)',
   '960.850 (+4.500)'],
  ['50',
   '50.894.400 (+350.000)',
   '1.017.888 (+7.000)',
   '48.095.000 (+225.000)',
   '961.900 (+4.500)'],
  ['25',
   '25.486.500 (+175.000)',
   '1.019.460 (+7.000)',
   '24.150.000 (+112.500)',
   '966.000 (+4.500)'],
  ['10',
   '10.244.800 (+70.000)',
   '1.024.480 (+7.000)',
   '9.710.000 (+45.000)',
   '971.000 (+4.500)'],
  ['5',
   '5.149.700 (+35.000)',
   '1.029.940 (+7.000)',
   '4.907.000 (+22.500)',
   '981.400 (+4.500)'],
  ['1',
   '1.074.800 (+7.000)',
   '1.074.800 (+7.000)',
   '1.014.000 (+4.500)',
   '1.014.000 (+4.500)'],
  ['', 'Update :18 September 2023, pukul 11:02']],
 [['Konversi Satuan'],
  ['Satuan', 'Ounce (oz)', 'Gram (gr)', 'Kilogram (kg)'],
  ['Ounce\xa0(oz)', '1', '31,1034767696', '0,0311034768'],
  ['Gram\xa0(gr)', '0,0321507466', '1', '0.001'],
  ['Kilogram\xa0(kg)', '32,1507466000', '1.000', '1']],
 [['Pergerakan Harga Emas Dunia'],
  ['Waktu', 'Emas'],
  ['Unit', 'USD', 'IDR'],
  ['Angka', '+/-', 'Angka', '+/-'],
  ['Hari Ini', 'Kurs', '', '', '15.140', '%'],
  ['oz', '1.923,78', '+2,18+0,11%', '29.126.029', '+33.005+0,11%'],
  ['gr', '61,85', '+0,07+0,11%', '936.424', '+1.061+0,11%'],
  ['30 Hari', 'Kurs', '', '', '15.731', '-591-3,76%'],
  ['oz', '1.823,86', '+102,10+5,60%', '28.691.142', '+467.893+1,63%'],
  ['gr', '58,64', '+3,28+5,60%', '922.442', '+15.043+1,63%'],
  ['2 Bulan', 'Kurs', '', '', '15.731', '-591-3,76%'],
  ['oz', '1.823,86', '+102,10+5,60%', '28.691.142', '+467.893+1,63%'],
  ['gr', '58,64', '+3,28+5,60', '922.442', '+15.043+1,63%'],
  ['6 Bulan', 'Kurs', '', '', '15.731', '-591-3,76%'],
  ['oz', '1.823,86', '+102,10+5,60%', '28.691.142', '+467.893+1,63%'],
  ['gr', '58,64', '+3,28+5,60%', '922.442', '+15.043+1,63%'],
  ['1 Tahun', 'Kurs', '', '', '14.899', '+241+1,62%'],
  ['oz', '1.675,23', '+250,73+14,97%', '24.959.252', '+4.199.783+16,83%'],
  ['gr', '53,86', '+8,06+14,97%', '802.459', '+135.026+16,83%'],
  ['2 Tahun', 'Kurs', '', '', '14.238', '+902+6,34%'],
  ['oz', '1.754,86', '+171,10+9,75%', '24.985.697', '+4.173.338+16,70%'],
  ['gr', '56,42', '+5,50+9,75%', '803.309', '+134.176+16,70%'],
  ['3 Tahun', 'Kurs', '', '', '14.768', '+372+2,52%'],
  ['oz', '1.958,50', '-32,54-1,66%', '28.923.128', '+235.906+0,82%'],
  ['gr', '62,97', '-1,05-1,66%', '929.900', '+7.585+0,82%'],
  ['5 Tahun', 'Kurs', '', '', '14.896', '+244+1,64%'],
  ['oz', '1.204,29', '+721,67+59,92%', '17.939.104', '+11.219.931+62,54%'],
  ['gr', '38,72', '+23,20+59,92%', '576.756', '+360.729+62,54%']])
(['Home', 'Emas 1 Gram', 'History', 'Trend', 'Perak 1 Gram', 'Pluang'],
 [[''],
  ['Emas 24 KaratHarga Emas 1 Gram', ''],
  ['USD', '61,92↑', '+0,07+0,11%'],
  ['KURS', '15.379,45↑', '+12,45+0,08%'],
  ['IDR', '952.311,72↑', '+1.847,97+0,19%'],
  ['Senin, 18 September 2023 21:21']],
 [[''],
  ['Emas 1 Gram (IDR)Emas 1 Gram (USD)Kurs USD-IDR',
   'Hari Ini',
   '1 Bulan',
   '1 Tahun',
   '5 Tahun',
   'Max',
   '']],
 [['Pergerakkan Harga Emas 1 Gram'],
  ['', 'Penutupan Kemarin', 'Pergerakkan Hari Ini', 'Rata-rata'],
  ['USD', '61,85', '61,85 - 61,92', '61,89'],
  ['KURS', '15.367,00', '15.367,00 - 15.379,45', '15.373,23'],
  ['IDR', '950.463,75', '950.463,75 - 952.311,72', '951.387,74'],
  [''],
  ['', 'Awal Tahun', 'Pergerakkan YTD', '+/- YTD'],
  ['USD', '58,64', '58,23 - 65,97', '+3,28 (5,59%)'],
  ['KURS', '15.538,50', '14.669,40 - 15.629,15', '-159,05(-1,02%)'],
  ['IDR', '911.153,72', '888.842,84 - 982.694,10', '+41.158,00 (4,52%)'],
  [''],
  ['', 'Tahun Lalu / 52 Minggu', 'Pergerakkan 52 Minggu', '+/- 52 Minggu'],
  ['USD', '53,86', '52,31 - 65,97', '+8,06 (14,96%)'],
  ['KURS', '14.999,20', '14.669,40 - 15.785,40', '+380,25 (2,54%)'],
  ['IDR', '807.855,34', '795.009,21 - 982.694,10', '+144.456,38 (17,88%)']])
```

## input_char

`input_char(prompt=None, prompt_ending='', newline_after_input=True, echo_char=True, default=None)`

Meminta masukan satu huruf tanpa menekan Enter.  

```py  
input_char("Input char : ")  
input_char("Input char : ", default='Y')  
input_char("Input Char without print : ", echo_char=False)  
```

## iopen

`iopen(path, data=None, regex=None, css_select=None, xpath=None, file_append=False)`

Membaca atau Tulis pada path yang bisa merupakan FILE maupun URL.  

Baca File :  
- Membaca seluruh file.  
- Jika berhasil content dapat diparse dengan regex.  
- Apabila File berupa html, dapat diparse dengan css atau xpath.  

Tulis File :  
- Menulis pada file.  
- Jika file tidak ada maka akan dibuat.  
- Jika file memiliki content maka akan di overwrite.  

Membaca URL :  
- Mengakses URL dan mengembalikan isi html nya berupa teks.  
- Content dapat diparse dengan regex, css atau xpath.  

Tulis URL :  
- Mengirimkan data dengan metode POST ke url.  
- Jika berhasil dan response memiliki content, maka dapat diparse  
  dengan regex, css atau xpath.  


```python  
# FILE  
print(iopen("__iopen.txt", "mana aja"))  
print(iopen("__iopen.txt", regex="(\w+)"))  
# URL  
print(iopen("https://www.google.com/", css_select="a"))  
print(iopen("https://www.google.com/", dict(coba="dulu"), xpath="//a"))  
```

Output:
```py
8
['mana', 'aja']
[<Element a at 0x77625e7200>, <Element a at 0x7762643070>, <Element a at 0x7762643110>, <Element a at 0x7762643160>, <Element a at 0x77626431b0>, <Element a at 0x7762643200>, <Element a at 0x7762643250>, <Element a at 0x77626432a0>, <Element a at 0x77626432f0>, <Element a at 0x7762643340>, <Element a at 0x7762643390>, <Element a at 0x77626433e0>, <Element a at 0x7762643430>, <Element a at 0x7762643480>, <Element a at 0x77626434d0>, <Element a at 0x7762643520>, <Element a at 0x7762643570>, <Element a at 0x77626435c0>]
False
```

## iprint

`iprint(*args, color=None, sort_dicts=False, **kwargs)`

Improve print function dengan menambahkan color dan pretty print  
Color menggunakan colorama Fore + Back + Style  

```python  
iprint(  
    'yang ini',  
    {'12':12,'sdsd':{'12':21,'as':[88]}},  
    color=colorama.Fore.BLUE + colorama.Style.BRIGHT  
)  
```

Output:
```py
[34m[1myang ini[0m [34m[1m{'12': 12, 'sdsd': {'12': 21, 'as': [88]}}[0m
```

## irange

`irange(start, finish, step=1)`

Meningkatkan fungsi range() dari python untuk pengulangan menggunakan huruf  

```python  
print(irange('a', 'c'))  
print(irange('z', 'a', 10))  
print(list(irange('a', 'z', 10)))  
print(list(irange(1, '7')))  
print(list(irange(10, 5)))  
```

Output:
```py
<generator object irange at 0x7762f13ab0>
<generator object irange at 0x7762f13ab0>
['a', 'k', 'u']
[1, 2, 3, 4, 5, 6, 7]
[10, 9, 8, 7, 6, 5]
```

## ireplace

`ireplace(string: str, replacements: dict, flags=re.IGNORECASE|re.MULTILINE|re.DOTALL)`

STRing TRanslate mengubah string menggunakan kamus dari dict.  
Replacement dapat berupa text biasa ataupun regex pattern.  
Apabila replacement berupa regex, gunakan raw string `r"..."`  
Untuk regex capturing gunakan `(...)`, dan untuk mengaksesnya  
gunakan `\1`, `\2`, .., dst.  

```python  
text = 'aku ini mau ke sini'  
replacements = {  
    "sini": "situ",  
    r"(ini)": r"itu dan \1",  
}  
print(ireplace(text, replacements))  
```

Output:
```py
aku itu dan ini mau ke situ
```

## is_empty

`is_empty(variable, empty=[None, False, 0, 0, '0', '', '-0', '\n', '\t', set(), {}, [], ()])`

Mengecek apakah variable setara dengan nilai kosong pada empty.  

Pengecekan nilai yang setara menggunakan simbol '==', sedangkan untuk  
pengecekan lokasi memory yang sama menggunakan keyword 'is'  

```python  
print(is_empty("teks"))  
print(is_empty(True))  
print(is_empty(False))  
print(is_empty(None))  
print(is_empty(0))  
print(is_empty([]))  
```

Output:
```py
False
False
True
True
True
True
```

## is_iterable

`is_iterable(var, str_is_iterable=False)`

Mengecek apakah suatu variabel bisa dilakukan forloop atau tidak  

```python  
s = 'ini string'  
print(is_iterable(s))  

l = [12,21,2,1]  
print(is_iterable(l))  

r = range(100)  
print(is_iterable(r))  

d = {'a':1, 'b':2}  
print(is_iterable(d.values()))  
```

Output:
```py
False
True
True
True
```

## is_valid_url

`is_valid_url(path)`

Mengecek apakah path merupakan URL yang valid atau tidak.  
Cara ini merupakan cara yang paling efektif.  

```python  
print(is_valid_url("https://chat.openai.com/?model=text-davinci-002-render-sha"))  
print(is_valid_url("https://chat.openai.com/?model/=text-dav/inci-002-render-sha"))  
```

Output:
```py
True
True
```

## iscandir

`iscandir(folder_name='.', glob_pattern='*', recursive=True, scan_file=True, scan_folder=True)`

Mempermudah scandir untuk mengumpulkan folder dan file.  

```python  
print(iscandir())  
print(list(iscandir("./", recursive=False, scan_file=False)))  
```

Output:
```py
<generator object iscandir at 0x77625d9640>
[PosixPath('dist'), PosixPath('.git'), PosixPath('pypipr'), PosixPath('__pycache__'), PosixPath('.vscode')]
```

## isplit

`isplit(text, separator='', include_separator=False)`

Memecah text menjadi list berdasarkan separator.  

```python  
t = '/ini/contoh/path/'  
print(isplit(t, separator='/'))  
```

Output:
```py
['', 'ini', 'contoh', 'path', '']
```

## log

`log(text=None)`

Decorator untuk mempermudah pembuatan log karena tidak perlu mengubah  
fungsi yg sudah ada.  
Melakukan print ke console untuk menginformasikan proses yg sedang  
berjalan didalam program.  

```py  
@log  
def some_function():  
    pass  

@log()  
def some_function_again():  
    pass  

@log("Calling some function")  
def some_function_more():  
    pass  

some_function()  
some_function_again()  
some_function_more()  
```

## password_generator

`password_generator(length=8, characters=None)`

Membuat pssword secara acak  

```python  
print(password_generator())  
```

Output:
```py
'/'SCe@4
```

## pip_freeze_without_version

`pip_freeze_without_version(filename=None)`

Memberikan list dari dependencies yang terinstall tanpa version.  
Bertujuan untuk menggunakan Batteries Included Python.  

```py  
print(pip_freeze_without_version())  
```

## poetry_publish

`poetry_publish(token=None)`

Publish project to pypi,org  

```py  
poetry_publish()  
```

## poetry_update_version

`poetry_update_version(mayor=False, minor=False, patch=True)`

Update versi pada pyproject.toml menggunakan poetry  

```py  
poetry_update_version()  
```

## print_colorize

`print_colorize(text, color='\x1b[32m', bright='\x1b[1m', color_end='\x1b[0m', text_start='', text_end='\n')`

Print text dengan warna untuk menunjukan text penting  

```py  
print_colorize("Print some text")  
print_colorize("Print some text", color=colorama.Fore.RED)  
```

## print_dir

`print_dir(var, colorize=True)`

Print property dan method yang tersedia pada variabel  

```python  
p = pathlib.Path("https://www.google.com/")  
print_dir(p, colorize=False)  
```

Output:
```py
           __bytes__ : b'https:/www.google.com'
           __class__ : .
             __dir__ : ['__module__', '__doc__', '__slots__', '__new__', '_make_child_relpath', '__enter__', '__exit__', 'cwd', 'home', 'samefile', 'iterdir', '_scandir', 'glob', 'rglob', 'absolute', 'resolve', 'stat', 'owner', 'group', 'open', 'read_bytes', 'read_text', 'write_bytes', 'write_text', 'readlink', 'touch', 'mkdir', 'chmod', 'lchmod', 'unlink', 'rmdir', 'lstat', 'rename', 'replace', 'symlink_to', 'hardlink_to', 'link_to', 'exists', 'is_dir', 'is_file', 'is_mount', 'is_symlink', 'is_block_device', 'is_char_device', 'is_fifo', 'is_socket', 'expanduser', '__reduce__', '_parse_args', '_from_parts', '_from_parsed_parts', '_format_parsed_parts', '_make_child', '__str__', '__fspath__', 'as_posix', '__bytes__', '__repr__', 'as_uri', '_cparts', '__eq__', '__hash__', '__lt__', '__le__', '__gt__', '__ge__', 'drive', 'root', 'anchor', 'name', 'suffix', 'suffixes', 'stem', 'with_name', 'with_stem', 'with_suffix', 'relative_to', 'is_relative_to', 'parts', 'joinpath', '__truediv__', '__rtruediv__', 'parent', 'parents', 'is_absolute', 'is_reserved', 'match', '_cached_cparts', '_drv', '_hash', '_parts', '_pparts', '_root', '_str', '__getattribute__', '__setattr__', '__delattr__', '__ne__', '__init__', '__reduce_ex__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__', '_flavour']
             __doc__ : Path subclass for non-Windows systems.

    On a POSIX system, instantiating a Path should return this object.
    
           __enter__ : https:/www.google.com
          __fspath__ : https:/www.google.com
        __getstate__ : (None, {'_drv': '', '_root': '', '_parts': ['https:', 'www.google.com'], '_str': 'https:/www.google.com'})
            __hash__ : 2836682788812097985
            __init__ : None
   __init_subclass__ : None
          __module__ : pathlib
          __reduce__ : (<class 'pathlib.PosixPath'>, ('https:', 'www.google.com'))
            __repr__ : PosixPath('https:/www.google.com')
          __sizeof__ : 72
           __slots__ : ()
             __str__ : https:/www.google.com
    __subclasshook__ : NotImplemented
      _cached_cparts : ['https:', 'www.google.com']
             _cparts : ['https:', 'www.google.com']
                _drv : 
            _flavour : <pathlib._PosixFlavour object at 0x776520fcd0>
               _hash : 2836682788812097985
              _parts : ['https:', 'www.google.com']
               _root : 
                _str : https:/www.google.com
            absolute : /data/data/com.termux/files/home/pypipr/https:/www.google.com
              anchor : 
            as_posix : https:/www.google.com
                 cwd : /data/data/com.termux/files/home/pypipr
               drive : 
              exists : False
          expanduser : https:/www.google.com
                home : /data/data/com.termux/files/home
         is_absolute : False
     is_block_device : False
      is_char_device : False
              is_dir : False
             is_fifo : False
             is_file : False
            is_mount : False
         is_reserved : False
           is_socket : False
          is_symlink : False
             iterdir : <generator object Path.iterdir at 0x7762d78ba0>
            joinpath : https:/www.google.com
                name : www.google.com
              parent : https:
             parents : <PosixPath.parents>
               parts : ('https:', 'www.google.com')
             resolve : /data/data/com.termux/files/home/pypipr/https:/www.google.com
                root : 
                stem : www.google
              suffix : .com
            suffixes : ['.google', '.com']
```

## print_log

`print_log(text)`

Akan melakukan print ke console.  
Berguna untuk memberikan informasi proses program yg sedang berjalan.  

```py  
print_log("Standalone Log")  
```

## random_bool

`random_bool()`

Menghasilkan nilai random True atau False.  
Fungsi ini merupakan fungsi tercepat untuk mendapatkan random bool.  
Fungsi ini sangat cepat, tetapi pemanggilan fungsi ini membutuhkan  
overhead yg besar.  

```python  
print(random_bool())  
```

Output:
```py
True
```

## set_timeout

`set_timeout(interval, func, args=None, kwargs=None)`

Menjalankan fungsi ketika sudah sekian detik.  
Apabila timeout masih berjalan tapi kode sudah selesai dieksekusi semua, maka  
program tidak akan berhenti sampai timeout selesai, kemudian fungsi dijalankan,  
kemudian program dihentikan.  

```python  
set_timeout(3, lambda: print("Timeout 3"))  
x = set_timeout(7, print, args=["Timeout 7"])  
print(x)  
print("menghentikan timeout 7")  
x.cancel()  
```

Output:
```py
<Timer(Thread-2, started 512724286720)>
menghentikan timeout 7
```

## sets_ordered

`sets_ordered(iterator)`

Hanya mengambil nilai unik dari suatu list  

```python  
array = [2, 3, 12, 3, 3, 42, 42, 1, 43, 2, 42, 41, 4, 24, 32, 42, 3, 12, 32, 42, 42]  
print(sets_ordered(array))  
print(list(sets_ordered(array)))  
```

Output:
```py
<generator object sets_ordered at 0x7762e4bac0>
[2, 3, 12, 42, 1, 43, 41, 4, 24, 32]
```

## str_cmp

`str_cmp(t1, t2)`

Membandingakan string secara incase-sensitive menggunakan lower().  
Lebih cepat dibandingkan upper(), casefold(), re.fullmatch(), len().  
perbandingan ini sangat cepat, tetapi pemanggilan fungsi ini membutuhkan  
overhead yg besar.  

```python  
print(str_cmp('teks1', 'Teks1'))  
```

Output:
```py
True
```

## text_colorize

`text_colorize(text, color='\x1b[32m', bright='\x1b[1m', color_end='\x1b[0m')`

return text dengan warna untuk menunjukan text penting  

```py  
text_colorize("Print some text")  
text_colorize("Print some text", color=colorama.Fore.RED)  
```

## to_str

`to_str(value)`

Mengubah value menjadi string literal  

```python  
print(to_str(5))  
print(to_str([]))  
print(to_str(False))  
print(to_str(True))  
print(to_str(None))  
```

Output:
```py
5

False
True

```

# CLASS

## APIMixinView

`APIMixinView`

APIView adalah class view untuk membuat Website API  
Cara kerjanya adalah dengan menggunakan variabel GET untuk menerima data.  
  
Class ini tidak bisa digunakan sendiri.  
Class ini harus menjadi mixin Class View karena perlu trigger untuk  
memanggil method get().  
  
```py  
class ExampleAPIView(APIMixinView, View):  
    pass  
```

## ComparePerformance

`ComparePerformance`

Menjalankan seluruh method dalam class,  
Kemudian membandingkan waktu yg diperlukan.  
Nilai 100 berarti yang tercepat.  
  
```python  
class ExampleComparePerformance(ComparePerformance):  
    # number = 1  
    z = 10  
  
    def a(self):  
        return (x for x in range(self.z))  
  
    def b(self):  
        return tuple(x for x in range(self.z))  
  
    def c(self):  
        return [x for x in range(self.z)]  
  
    def d(self):  
        return list(x for x in range(self.z))  
  
pprint.pprint(ExampleComparePerformance().compare_result(), depth=100)  
print(ExampleComparePerformance().compare_performance())  
print(ExampleComparePerformance().compare_performance())  
print(ExampleComparePerformance().compare_performance())  
print(ExampleComparePerformance().compare_performance())  
print(ExampleComparePerformance().compare_performance())  
```

Output:
```py
{'a': <generator object ExampleComparePerformance.a.<locals>.<genexpr> at 0x7762e4a4d0>,
 'b': (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
 'c': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 'd': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
```

## HttpResponse

`HttpResponse`

An HTTP response class with a string as content.  
  
This content can be read, appended to, or replaced.

## PintUregQuantity

`PintUregQuantity`

## RunParallel

`RunParallel`

Menjalankan program secara bersamaan.  
  
- `class RunParallel` didesain hanya untuk pemrosesan data saja.  
- Penggunaannya `class RunParallel` dengan cara membuat instance  
  sub class beserta data yg akan diproses, kemudian panggil fungsi  
  yg dipilih `run_asyncio / run_multi_threading / run_multi_processing`,  
  kemudian dapatkan hasilnya.  
- `class RunParallel` tidak didesain untuk menyimpan data, karena  
  setiap module terutama module `multiprocessing` tidak dapat mengakses  
  data kelas dari proses yg berbeda.  
- Semua methods akan dijalankan secara paralel kecuali method dengan  
  nama yg diawali underscore `_`  
- Method untuk multithreading/multiprocessing harus memiliki 2  
  parameter, yaitu: `result: dict` dan `q: queue.Queue`. Parameter  
  `result` digunakan untuk memberikan return value dari method, dan  
  Parameter `q` digunakan untuk mengirim data antar proses.  
- Method untuk asyncio harus menggunakan keyword `async def`, dan  
  untuk perpindahan antar kode menggunakan `await asyncio.sleep(0)`,  
  dan keyword `return` untuk memberikan return value.  
- Return Value berupa dictionary dengan key adalah nama function,  
  dan value adalah return value dari setiap fungsi  
- Menjalankan Multiprocessing harus berada dalam blok  
  `if __name__ == "__main__":` karena area global pada program akan  
  diproses lagi. Terutama pada sistem operasi windows.  
- `run_asyncio()` akan menjalankan kode dalam satu program, hanya  
  saja alur program dapat berpindah-pindah menggunkan  
  `await asyncio.sleep(0)`.  
- `run_multi_threading()` akan menjalankan program dalam satu CPU,  
  hanya saja dalam thread yang berbeda. Walaupun tidak benar-benar  
  berjalan secara bersamaan namun bisa meningkatkan kecepatan  
  penyelesaian program, dan dapat saling mengakses resource antar  
  program.  Akses resource antar program bisa secara langsung maupun  
  menggunakan parameter yang sudah disediakan yaitu `result: dict`  
  dan `q: queue.Queue`.  
- `run_multi_processing()` akan menjalankan program dengan beberapa  
  CPU. Program akan dibuatkan environment sendiri yang terpisah dari  
  program induk. Keuntungannya adalah program dapat benar-benar berjalan  
  bersamaan, namun tidak dapat saling mengakses resource secara langsung.  
  Akses resource menggunakan parameter yang sudah disediakan yaitu  
  `result: dict` dan `q: queue.Queue`.  
  
```python  
class ExampleRunParallel(RunParallel):  
    z = "ini"  
  
    def __init__(self) -> None:  
        self.pop = random.randint(0, 100)  
  
    def _set_property_here(self, v):  
        self.prop = v  
  
    def a(self, result: dict, q: queue.Queue):  
        result["z"] = self.z  
        result["pop"] = self.pop  
        result["a"] = "a"  
        q.put("from a 1")  
        q.put("from a 2")  
  
    def b(self, result: dict, q: queue.Queue):  
        result["z"] = self.z  
        result["pop"] = self.pop  
        result["b"] = "b"  
        result["q_get"] = q.get()  
  
    def c(self, result: dict, q: queue.Queue):  
        result["z"] = self.z  
        result["pop"] = self.pop  
        result["c"] = "c"  
        result["q_get"] = q.get()  
  
    async def d(self):  
        print("hello")  
        await asyncio.sleep(0)  
        print("hello")  
  
        result = {}  
        result["z"] = self.z  
        result["pop"] = self.pop  
        result["d"] = "d"  
        return result  
  
    async def e(self):  
        print("world")  
        await asyncio.sleep(0)  
        print("world")  
  
        result = {}  
        result["z"] = self.z  
        result["pop"] = self.pop  
        result["e"] = "e"  
        return result  
  
if __name__ == "__main__":  
    print(ExampleRunParallel().run_asyncio())  
    print(ExampleRunParallel().run_multi_threading())  
    print(ExampleRunParallel().run_multi_processing())  
```

## html_dl

`html_dl`

Class ini digunakan untuk idumps dan iloads html

## html_ol

`html_ol`

Class ini digunakan untuk idumps dan iloads html

## html_table

`html_table`

Class ini digunakan untuk idumps dan iloads html

## html_ul

`html_ul`

Class ini digunakan untuk idumps dan iloads html
