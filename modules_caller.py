import modules as mo
import datetime
import packages_demo.package_file as pa
import sample_package.sample1 as sa1
from modules import abc
# print(mo.abc("Joseph"))
print(abc("Joseph"))
pa.pack("Inside package")
print(dir(datetime))
print(sa1.sample_one())
