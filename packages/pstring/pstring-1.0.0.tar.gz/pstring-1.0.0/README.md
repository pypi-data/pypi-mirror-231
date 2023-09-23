# PString

PString is a Python package for working with IPA (International Phonetic Alphabet) symbols in strings. It addresses issues where standard Python string operations may not work as expected with IPA symbols, such as iterating over a string and accessing a symbol by its index. This happens because Python interprets some phonemes as multiple individual chars when dealing with standard strings.

## Installation

You can install PString using pip:

```bash
pip install pstring
```

Make sure you have the required Python version and any dependencies installed.

# PString
PString is a str class that recognizes **IPA symbols**.

Basic operations like iterating over a string and accessing a char by its index don't work well when using str to represent an IPA string, 
because Python interprets some phonemes as multiple individual chars.

PString recognizes IPA symbols and adapts these operations so that they work properly.

## Usage

Example:
```
from PString import PString

text = "bõ d͡ʒiɐ"
phones = PString(text)

print(f"{text}")
print(f"{phones}")
```

Output:
```
bõ d͡ʒiɐ
bõ d͡ʒiɐ
```

You can iterate over a PString and also create a list of phonemes:
```
for phone in phones:
    print(phone)

print(f"str list: {list(text)}")
print(f"PString list: {list(phones)}")
```

Output:
```
b
õ

d͡ʒ
i
ɐ
str list: ['b', 'õ', ' ', 'd', '͡', 'ʒ', 'i', 'ɐ']
PString list: ['b', 'õ', ' ', 'd͡ʒ', 'i', 'ɐ']
```

You can also access a specific position or slice of the PString:
```
print(phones[3])
print(phones[3:6])
```

Output:
```
d͡ʒ
d͡ʒiɐ
```

If you wish to convert a PString back to a str:
```
phones_string = phones.to_string()
print(phones_string)
print(phones_string == text)
```

Output:
```
bõ d͡ʒiɐ
True
```

## Disclaimer

This package should represent IPA symbols listed on [IPA symbols with Unicode decimal and hex codes](https://www.internationalphoneticalphabet.org/ipa-charts/ipa-symbols-with-unicode-decimal-and-hex-codes/). Any incompatibilities of encoding are not of the author's responsibility.

## License

This package is distributed under the MIT license. See the LICENSE file for details.