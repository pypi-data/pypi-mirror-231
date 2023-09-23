class PString(str):
    """Class that represents a string of IPA characters, treating
    characters followed by diacritics or suprasegmentals as single characters.
    """
    DIACRITICS_AND_SUPRASEGMENTALS = {'ʰ', 'ʼ', '̴', '̜', '͜', '̹', 'ˑ', '̋', '̪', 'ʲ', 
                                      'ʷ', '͡', '̀', '̠', '̃', '̙', 'ˈ', '̤', '̞', '̯', 
                                      '̈', '̥', 'ˌ', '̻', 'ʴ', '̼', '̚', '́', 'ʱ', '˞', 
                                      '̆', '̟', '̺', 'ː', '̝', 'ˤ', 'ˠ', '̰', '̊', '̏', 
                                      '̽', '̬', '̄', '̘', '̩'}
    COMBINATIONS = {'dʒ', 'lʒ', 'tʃ', 'd͡ʒ', 'l͡ʒ', 't͡ʃ'}

    def return_pstring_instance(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):
                return PString(result)
            return result
        return wrapper

    @return_pstring_instance
    def __iter__(self):
        # Iterate over the string 
        s = super().__str__()
        i = 0
        while i < len(s):
            start = i
            end = i+1
            while end < len(s):
                if s[start:end+1] in PString.COMBINATIONS \
                    or s[end] in PString.DIACRITICS_AND_SUPRASEGMENTALS:
                    end += 1
                else:
                    break
            yield s[start:end]
            i = end

    def __len__(self):
        # Compute the length directly within this method
        length = 0
        for _ in self:
            length += 1
        return length

    @return_pstring_instance
    def __getitem__(self, __key):
        # Get a substring
        return ''.join(list(self)[__key])

    def to_string(self):
        """
        Convert the PString to Python's str
        """
        return super().__str__()

    # Overriding str methods that return a str instance to return a PString instance

    @return_pstring_instance
    def capitalize(self):
        return super().capitalize()

    @return_pstring_instance
    def casefold(self):
        return super().casefold()

    @return_pstring_instance
    def center(self, *args, **kwargs):
        return super().center(*args, **kwargs)

    @return_pstring_instance
    def expandtabs(self, *args, **kwargs):
        return super().expandtabs(*args, **kwargs)

    @return_pstring_instance
    def format(self, *args, **kwargs):
        return super().format(*args, **kwargs)

    @return_pstring_instance
    def format_map(self, *args, **kwargs):
        return super().format_map(*args, **kwargs)

    @return_pstring_instance
    def join(self, *args, **kwargs):
        return super().join(*args, **kwargs)

    @return_pstring_instance
    def ljust(self, *args, **kwargs):
        return super().ljust(*args, **kwargs)

    @return_pstring_instance
    def lower(self):
        return super().lower()

    @return_pstring_instance
    def lstrip(self, *args, **kwargs):
        return super().lstrip(*args, **kwargs)

    @return_pstring_instance
    def replace(self, *args, **kwargs):
        return super().replace(*args, **kwargs)

    @return_pstring_instance
    def rjust(self, *args, **kwargs):
        return super().rjust(*args, **kwargs)

    @return_pstring_instance
    def rstrip(self, *args, **kwargs):
        return super().rstrip(*args, **kwargs)

    @return_pstring_instance
    def strip(self, *args, **kwargs):
        return super().strip(*args, **kwargs)

    @return_pstring_instance
    def swapcase(self):
        return super().swapcase()

    @return_pstring_instance
    def title(self):
        return super().title()

    @return_pstring_instance
    def translate(self, *args, **kwargs):
        return super().translate(*args, **kwargs)

    @return_pstring_instance
    def upper(self):
        return super().upper()
