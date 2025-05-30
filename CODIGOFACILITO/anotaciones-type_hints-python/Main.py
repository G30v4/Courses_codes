import random

# --- TIPOS BASICOS --- #
username: str
active: bool
altura: float = random.random() * (2 - 1) + 1
edad: int = random.randint(5,100)

username = 'G30v4'
active  = True
print(username, altura, edad, active) 

username = 304 # Para el interprete es irrelevante
print(username)


# --- None TYPE --- #
username: None = None
print(username)

# --- Listas, tuplas y diccionarios --- #
numbers: list = [1,2,4]
names: tuple = ('user1', 'user2')
scores: dict = {'user1': 100, 'user2': 70}

print(numbers, names, scores, sep = "\n")

## with typing
from typing import List, Tuple, Dict

numbers: List[int] = [1,2,4]
names: Tuple[str, str] = ('user1', 'user2')
scores: Dict[str, int] = {'user1': 100, 'user2': 70}
print(numbers, names, scores, sep = "\n")

setting: Tuple[bool, int, str] = (True, 3256, 'root')
print(setting)

# --- FUNCIONES --- #
def average(numbers: List[int]) -> float:
    return sum(numbers) / len(numbers)

scores: List[int] = [10,9,10,8,9,8]   
result: float = average(scores)
print(result)

def _sum(num_1, num_2):
    return num_1 + num_2

# Evita la ambiguedad, solo a nivel visual del programador
def _sum2(num_1: int, num_2: int) -> int:
    return num_1 + num_2
    
print(_sum(5,12))
print(_sum('Hello', 'G30v4')) #ambiguedad


# --- CONSTANTES --- #
from typing import  Final

SETTINGS: Final = (True, 'root', 2144)
print(SETTINGS)


# --- UNION --- #
from typing import  Union

username: Union[None, str] # Puede ser de uno de los dos tipos descritos, de forma explicita

def average(numbers: List[int]) -> Union[None, float]:
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

## with pipes, apply in v3.9+
def average2(numbers: List[int]) -> None | float:
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

numbers = []
result: Union[None, float] = average(numbers)
print(result)

## with pipes
numbers2 = [2,4,6,8,9]
result2: None | float = average2(numbers2)
print(result2)


# --- ANY --- #
from typing import  Any, Optional

x: Any # Puede ser de cualquier tipo de dato, de forma explicita

def foo(param: Any) -> Any:
    pass

# Función con parametros opcionales
def foo2(param: Optional[int] = 10) -> int:
    return param
    
print(foo2())
print(foo2(10.3))


# --- ALIAS --- #
ConnectionType = Tuple[str, str, int]
UserIdOrNone = int | None

def db_connection(conn: ConnectionType) -> ConnectionType | None:
    if conn[0] != 'root':
        return None
    return conn

conn1: ConnectionType = ('root', 'mydb', 3030)
conn2: ConnectionType = ('g30v4', 'mydb', 3030) 
print(db_connection(conn1))
print(db_connection(conn2))

# --- LITERALS --- #
from typing import  Literal

# Enums -  since v3.11+
ColorsEnum = Literal['red', 'green', 'blue', 'white', 'black']
GenderEnum = Literal['M', 'F']
PermissionEnum = Literal['r', 'rb', 'w', 'wb']

def set_backgroud_color(color: ColorsEnum):
    pass

def make_user(username: str, email: str, gender: GenderEnum):
    pass

def open_handler(file: str, mode: PermissionEnum):
    pass


# --- TIPOS DE CLASES --- #
class User:
    
    def __init__(self, username: str, email: str) -> None:
        self.username: str = username
        self.email: str = email
        
def make_user(username: str, email: str) -> User:
    return User(username, email)
    
user1: User = make_user('G30v4', 'mail@email.com')
print(user1.username)
print(user1.email)


# --- TIPOS DE DATO SELF --- #
from typing import Self # Self since v3.11

class User2:
    
    def __init__(self, username: str, email: str) -> None:
        self.username: str = username
        self.email: str = email
        
    def copy(self) -> Self: # Rotanrna objeto del mismo tipo de la clase
        return User2(self.username, self.email)
        
    def get_user(self) -> Self:
        return self
        
    def __str__(self) -> str:
        return f'{self.username} - {self.email}'
    
user1: User2 = User2('G30v4', 'mail@email.com')
user_copy = user1.copy()
user2 = user1.get_user()
print(user1)
print(user_copy)
print(user2)


# --- TIPO NamedTuple --- #
from typing import NamedTuple 

class DBSettings(NamedTuple):
    
    username: str
    password: str | None
    port: Literal[3306, 3307, 3308]
    db: str
    
db_config = DBSettings(
    'g30v4',
    'pass123',
    3423,
    'mydb'
    ) 
    
print(db_config.username)
print(db_config.db)

#db_config.password = '123456' # No permitido
#db_config.timeout = 12 # No permitido


# --- TIPO TypeVar --- #
from typing import TypeVar

T = TypeVar('T')

def first_element(collection: List[T]) -> T | None:
    """Retorna el primer elemento de la lista"""
    if len(collection) == 0:
        return None
    return collection[0]
    
print(first_element(['User1', 'User2', 'User3']))
print(first_element([8, 10, 5]))

# Mas especifico o personalizado, generico
Number = TypeVar('Number', int, float)
Collection = TypeVar('Collection', List, Tuple, Dict)

def double(num: Number) -> Number:
    return num * 2
    
result: Number = double(5)
print(result)