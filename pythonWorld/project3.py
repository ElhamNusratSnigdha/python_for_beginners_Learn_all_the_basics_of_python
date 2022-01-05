def encrypt(sentence):
    encryption = ""
    for element in sentence:
        if element in "Aa":
            encryption=encryption+"1"
        elif element in 'Bb':
            encryption=encryption+'2'
        elif element in 'Cc':
            encryption=encryption+'3'
        elif element in 'Dd':
            encryption=encryption+'4'
        elif element in 'Ee':
            encryption=encryption+'5'
        elif element in 'Ff':
            encryption=encryption+'6'
        elif element in 'Gg':
            encryption=encryption+'7'
        elif element in 'Hh':
            encryption=encryption+'8'
        elif element in 'Ii':
            encryption=encryption+'9'
        elif element in 'Jj':
            encryption=encryption+'10'
        elif element in 'Kk':
            encryption=encryption+'11'
        elif element in 'Ll':
            encryption=encryption+'12'
        elif element in 'Mm':
            encryption=encryption+'13'
        elif element in 'Nn':
            encryption=encryption+'14'
        elif element in 'Oo':
            encryption=encryption+'15'
        elif element in 'Pp':
            encryption=encryption+'16'
        elif element in 'Qq':
            encryption=encryption+'17'
        elif element in 'Rr':
            encryption=encryption+'18'
        elif element in 'Ss':
            encryption=encryption+'19'
        elif element in 'Tt':
            encryption=encryption+'20'
        elif element in 'Uu':
            encryption=encryption+'21'
        elif element in 'Vv':
            encryption=encryption+'22'
        elif element in 'Ww':
            encryption=encryption+'23'
        elif element in 'Xx':
            encryption=encryption+'24'
        elif element in 'Yy':
            encryption=encryption+'25'
        elif element in 'Zz':
            encryption=encryption+'26'
        else:encryption=encryption+element

    return encryption

print(encrypt(input("Send your message:")))