
class Dictionaries:
    def __init__(self):
        pass

    def animals(self):
        self.animals = {'a': ['aardvark', 'antelope', 'alpaca', 'anaconda', 'anteater'],
                        'b': ['bear', 'buffalo', 'bat', 'beaver', 'baboon'],
                        'c': ['cat', 'crocodile', 'chimpanzee', 'camel', 'crab','cockroach','capybara'],
                        'd': ['dog', 'dolphin', 'donkey', 'deer', 'duck'],
                        'e': ['elephant', 'emu', 'eel', 'eagle', 'elk'],
                        'f': ['fox', 'ferret', 'flamingo', 'frog', 'fish'],
                        'g': ['goat', 'gorilla', 'gecko', 'giraffe', 'grasshopper'],
                        'h': ['horse', 'hippopotamus', 'hyena', 'hawk', 'hamster'],
                        'i': ['iguana', 'impala', 'ibex', 'indri', 'insect'],
                        'j': ['jaguar', 'jackal', 'jellyfish', 'javelin', 'jay'],
                        'k': ['kangaroo', 'koala', 'kudu', 'kiwi', 'kingfisher'],
                        'l': ['lion', 'lemur', 'llama', 'lynx', 'lobster'],
                        'm': ['monkey', 'moose', 'mongoose', 'mouse', 'magpie'],
                        'n': ['newt', 'nightingale', 'numbat', 'narwhal', 'nuthatch'],
                        'o': ['otter', 'octopus', 'orangutan', 'ostrich', 'owl'],
                        'p': ['panda', 'panther', 'porcupine', 'penguin', 'parrot'],
                        'q': ['quokka', 'quail', 'quetzal', 'quokka', 'quoll'],
                        'r': ['rhinoceros', 'rabbit', 'rat', 'reindeer', 'raccoon'],
                        's': ['snake', 'sheep', 'seagull', 'sloth', 'swan'],
                        't': ['tiger', 'turtle', 'toucan', 'turkey', 'tarantula'],
                        'u': ['umbrellabird', 'urial', 'unicorn', 'urchin', 'ungulate'],
                        'v': ['vulture', 'vicuna', 'vaquita', 'viper', 'vole'],
                        'w': ['whale', 'weasel', 'walrus', 'wombat', 'woodpecker'],
                        'x': ['xerus', 'xenarthra', 'xenopus', 'xoloitzcuintli'],
                        'y': ['yak', 'yabby', 'yellowjacket', 'yaksha', 'yeti'],
                        'z': ['zebra', 'zorilla', 'zebu', 'zeedonk']
                    }
        return self.animals

    # towns or capitals
    def places(self):
        self.places = {'a': ['amsterdam', 'ankara', 'adelaide', 'athens'],
                        'b': ['brasilia', 'berlin', 'bangkok', 'budapest', 'buenos aires'],
                        'c': ['canberra', 'copenhagen', 'cape town', 'caracas', 'chicago'],
                        'd': ['dakar', 'dublin', 'dhaka', 'doha', 'detroit'],
                        'e': ['edinburgh', 'eindhoven', 'erbil', 'esfahan'],
                        'f': ['frankfurt', 'freetown', 'florence', 'fortaleza', 'fukuoka'],
                        'g': ['guatemala city', 'geneva', 'georgetown', 'gaborone', 'gaziantep'],
                        'h': ['havana', 'helsinki', 'hargeisa', 'houston', 'harare'],
                        'i': ['islamabad', 'istanbul', 'innsbruck', 'iquitos', 'izmir'],
                        'j': ['jakarta', 'jerusalem', 'jeddah', 'johannesburg', 'juneau'],
                        'k': ['kabul', 'kathmandu', 'kigali', 'kingston', 'kuwait city'],
                        'l': ['london', 'lisbon', 'lima', 'ljubljana'],
                        'm': ['moscow', 'madrid', 'manila', 'montreal'],
                        'n': ['nairobi', 'naples', 'nashville', 'nouakchott'],
                        'o': ['oslo', 'ottawa', 'ouagadougou', 'odessa', 'oranjestad'],
                        'p': ['paris', 'prague', 'perth'],
                        'q': ['quebec', 'quito', 'quetzaltenango', 'qom', 'qufu'],
                        'r': ['riyadh', 'rome', 'rio de janeiro', 'reykjavík', 'riga'],
                        's': ['seoul', 'singapore', 'stockholm', 'san francisco', 'sao paulo'],
                        't': ['tokyo', 'tehran', 'taipei', 'toronto', 'tunis'],
                        'u': ['ulaanbaatar', 'utrecht', 'ushuaia', 'uberlandia'],
                        'v': ['vienna', 'vilnius', 'valletta', 'victoria', 'vientiane'],
                        'w': ['warsaw', 'wellington', 'wuhan', 'winnipeg'],
                        'x': ['xiamen', 'xinyang', 'xalapa', 'xuzhou'],
                        'y': ['yangon', 'yerevan', 'yaoundé', 'yogyakarta', 'yakutsk'],
                        'z': ['zagreb', 'zurich', 'zaragoza', 'zamboanga', 'zanzibar']
                    }
        return self.places


    # fruits
    def fruits(self):
        self.fruits = {'a': ['apple', 'apricot', 'avocado', 'ackee', 'acai', 'abiu', 'ambarella'],
                    'b': ['banana', 'blackberry', 'blueberry', 'boysenberry', 'bilberry'],
                        'c': ['cherry', 'coconut', 'clementine', 'cantaloupe', 'cranberry'],
                        'd': ['date', 'dragonfruit', 'durian'],
                        'e': ['elderberry'],
                        'f': ['fig', 'feijoa'],
                        'g': ['gooseberry', 'grape', 'guava'],
                        'h': ['honeydew melon', 'huckleberry'],
                        'j': ['jackfruit', 'jambul', 'jujube'],
                        'k': ['kiwi', 'kumquat'],
                        'l': ['lemon', 'lime', 'lychee'],
                        'm': ['mango', 'mandarin orange', 'mulberry'],
                        'n': ['nectarine'], 
                        'o': ['orange'],
                        'p': ['papaya', 'passionfruit', 'peach', 'pear', 'pineapple', 'plum', 'pomegranate'],
                        'q': ['quince'],
                        'r': ['raspberry', 'redcurrant'],
                        's': ['starfruit', 'strawberry'],
                        't': ['tangerine', 'tomato'],
                        'u': ['ugli'],
                        'w': ['watermelon', 'wolfberry'],
                        'y': ['yuca', 'yumberry', 'yuzu'],
                        'z': ['zucchini', 'zante currants', 'zabaiion', 'zalacca', 'ziziphus mauritiana']
                    }
        return self.fruits
    
    # random
    def expert(self):
        self.expert = {'a': ['apple', 'ant', 'airplane', 'apricot', 'alligator', 'acorn', 'arrow'],
                    'b': ['ball', 'banana', 'book', 'bee', 'butterfly', 'bread'],
                        'c': ['cat', 'cup', 'car', 'cake', 'camel', 'candy', 'candle'],
                        'd': ['dog', 'duck', 'donut', 'dolphin', 'door', 'drum', 'dragon'],
                        'e': ['egg', 'elephant', 'ear', 'eel', 'engine', 'elbow', 'earth'],
                        'f': ['flower', 'fish', 'flag', 'fire', 'frog', 'fox', 'fan'],
                        'g': ['grape', 'goose', 'goat', 'gift', 'giraffe', 'guitar', 'garlic'],
                        'h': ['hat', 'hand', 'heart', 'hippo', 'horse', 'hamburger', 'helicopter'],
                        'i': ['ice', 'igloo', 'island', 'insect', 'ice cream', 'iron', 'iguana'],
                        'j': ['jacket', 'jam', 'jellyfish', 'jet', 'jeans', 'jester', 'jigsaw'],
                        'k': ['kangaroo', 'kite', 'key', 'kiwi', 'king', 'koala', 'ketchup'],
                        'l': ['lion', 'lemon', 'leaf', 'lollipop', 'lizard', 'lighthouse', 'lamb'],
                        'm': ['monkey', 'moon', 'mouse', 'muffin', 'mountain', 'mushroom', 'motorcycle'],
                        'n': ['nest', 'nose', 'nut', 'needle', 'necklace', 'night', 'net'],
                        'o': ['orange', 'octopus', 'ocean', 'ostrich', 'owl', 'onion', 'olive'],
                        'p': ['pig', 'pizza', 'pear', 'peacock', 'penguin', 'pencil', 'pumpkin'],
                        'q': ['queen', 'quilt', 'quail', 'quartz', 'quiver', 'quiet'],
                        'r': ['rabbit', 'rainbow', 'rose', 'robot', 'rhino', 'ring', 'rocket'],
                        's': ['sun', 'snake', 'star', 'snowman', 'squirrel', 'spider', 'smile'],
                        't': ['tree', 'tiger', 'trumpet', 'turtle', 'tomato', 'teapot', 'table'],
                        'u': ['umbrella', 'unicorn', 'ukulele', 'uncle', 'usher'],
                        'v': ['violin', 'van', 'vase', 'volcano', 'vegetable', 'vest', 'vacuum'],
                        'w': ['watermelon', 'whale', 'wagon', 'wheel', 'worm', 'witch', 'window'],
                        'x': ['xylophone', 'xylophone', 'x-ray', 'xenophobia', 'xanthan', 'xenon', 'xerography'],
                        'y': ['yellow', 'yoyo', 'yacht', 'yak', 'yawn', 'yogurt', 'yo-yo'],
                        'z': ['zebra', 'zoo', 'zealot', 'zipper', 'zucchini', 'zeppelin', 'zero', 'zesty']
                        }
        return self.expert
