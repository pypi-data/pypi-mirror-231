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
            yield PString(s[start:end])
            i = end

    def __len__(self):
        # Compute the length directly within this method
        length = 0
        for _ in self:
            length += 1
        return length

    def __getitem__(self, __key):
        # Get a substring
        return PString(''.join(list(self)[__key]))

    def to_string(self):
        """
        Convert the PString to Python's str
        """
        return super().__str__()