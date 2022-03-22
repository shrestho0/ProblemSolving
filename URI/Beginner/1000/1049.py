# Alhamdulillah, got accepted on the first attempt
# This was a critical one
bullshit_animals  = {
    'vertebrado' : {
        'ave' : {
            'carnivoro' : 'aguia',
            'onivoro' :  'pomba'
            },
            'mamifero': {
                'onivoro' : 'homem',
                'herbivoro' : 'vaca'
        }
    },

    'invertebrado' : {
        'inseto' : {
            'hematofago': 'pulga',
            'herbivoro' : 'lagarta'
        },
        'anelideo': {
            'hematofago' : 'sanguessuga',
            'onivoro' : 'minhoca'
        }
    }
    
}


one, two, three = [input() for x in range(3)]
the_bullshit_one = bullshit_animals.get(one).get(two).get(three)
print(the_bullshit_one)


