names = dict([(0, 'ZERO'),
              (1, 'ONE'),
              (2, 'TWO'),
              (3, 'THREE'),
              (4, 'FOUR'),
              (5, 'FIVE'),
              (6, 'SIX'),
              (7, 'SEVEN'),
              (8, 'EIGHT'),
              (9, 'NINE'),
              (10, 'TEN'),
              (11, 'ELEVEN'),
              (12, 'TWELVE'),
              (13, 'THIRTEEN'),
              (14, 'FOURTEEN'),
              (15, 'FIFTEEN'),
              (16, 'SIXTEEN'),
              (17, 'SEVENTEEN'),
              (18, 'EIGHTEEN'),
              (19, 'NINETEEN'),
              (20, 'TWENTY'),
              (30, 'THIRTY'),
              (40, 'FORTY'),
              (50, 'FIFTY'),
              (60, 'SIXTY'),
              (70, 'SEVENTY'),
              (80, 'EIGHTY'),
              (90, 'NINETY'),
              (100, 'HUNDRED'),
              (1000, 'THOUSAND')])

def text_from_num(cents):
    if (cents <= 0) or (cents > 99999999):
        raise(ValueError('invalid input'))
    num = int(cents)
    sb = []
    val = num - ((num // 100) * 100)
    if val in names:
        sb.append(names[val])
    else:
        tens = (val // 10) * 10
        ones = val - tens
        sb.append(names[ones])
        sb.append(names[tens])  
    sb.append('AND')
    
    num = num // 100
    val = num - ((num // 100) * 100)
    if val in names:
        sb.append(names[val])
    else:
        tens = (val // 10) * 10
        ones = val - tens
        sb.append(names[ones])
        sb.append(names[tens])
        
    num = num // 100
    val = num - ((num // 10) * 10)
    if (val > 0):
        if sb[len(sb)-1] == names[0]:
            sb.pop()
        sb.append(names[100])
        sb.append(names[val])
        
    num = num // 10
    if (num > 0):
        if sb[len(sb)-1] == names[0]:
            sb.pop()        
        sb.append(names[1000])
        
        val = num - ((num // 100) * 100)
        if val in names:
            sb.append(names[val])
        else:
            tens = (val // 10) * 10
            ones = val - tens
            sb.append(names[ones])
            sb.append(names[tens])        
        
        num = num // 100
        if (num > 0):
            if sb[len(sb)-1] == names[0]:
                sb.pop()
            sb.append(names[100])    
            sb.append(names[num])    
            
    return ' '.join(sb[::-1])



