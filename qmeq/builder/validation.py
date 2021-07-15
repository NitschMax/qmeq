"""Module containing methods for validation of input parameters."""


def validate_kerntype(kerntype):
    if isinstance(kerntype, str):
        if kerntype not in {'Pauli', 'Lindblad', 'Redfield', '1vN', '2vN',
                            'pyPauli', 'pyLindblad', 'pyRedfield', 'py1vN', 'py2vN'}:
            print("WARNING: Allowed kerntype values are: " +
                  "\'Pauli\', \'Lindblad\', \'Redfield\', \'1vN\', \'2vN\', " +
                  "\'pyPauli\', \'pyLindblad\', \'pyRedfield\', \'py1vN\', \'py2vN\'. " +
                  "Using default kerntype=\'Pauli\'.")
            kerntype = 'Pauli'
    return kerntype


def validate_itype(itype):
    if itype not in {0, 1, 2, 3}:
        print("WARNING: itype needs to be 0, 1, 2, or 3. Using default itype=0.")
        itype = 0
    return itype


def validate_itype_ph(itype_ph):
    if itype_ph not in {0, 2}:
        print("WARNING: itype_ph needs to be 0, or 2. Using default itype=0.")
        itype_ph = 0
    return itype_ph


def validate_indexing(indexing, symmetry, kerntype):
    if indexing is None:
        if symmetry is 'spin' and kerntype not in {'py2vN', '2vN'}:
            indexing = 'ssq'
        else:
            indexing = 'charge'

    if indexing not in {'Lin', 'charge', 'sz', 'ssq'}:
        print("WARNING: Allowed indexing values are: \'Lin\', \'charge\', \'sz\', \'ssq\'. " +
              "Using default indexing=\'charge\'.")
        indexing = 'charge'

    if indexing not in {'Lin', 'charge'} and kerntype in {'py2vN', '2vN'}:
        print("WARNING: For 2vN approach indexing needs to be \'Lin\' or \'charge\'. " +
              "Using indexing=\'charge\' as a default.")
        indexing = 'charge'

    return indexing

def validate_countingleads(countingleads): #simon
    if len(set(countingleads)) != len(countingleads):
        print('WARNING: The counting field gets attached more than once to at least one lead!')
    return countingleads
