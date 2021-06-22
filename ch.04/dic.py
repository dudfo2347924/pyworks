#딕셔너리

person = {}

person['이름'] = "이순신"
person['나이'] = 40
person['주소'] = "전라도"

for key in person:
    print(person[key])

del person['주소']
print(person)
