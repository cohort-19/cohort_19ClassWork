#Using dynamic concept of classes identify at least 7 classes with at least 7 properties/attributes and create at least 7 objects

#1.Creating a Fruit Class
class Fruit:
    def __init__(self, name, color, taste, weight, price, season, origin):
        self.name = name
        self.color = color
        self.taste = taste
        self.weight = weight
        self.price = price
        self.season = season
        self.origin = origin

# Creating objects for the Fruit class
apple = Fruit("Apple", "Red", "Sweet", 150, 1.2, "Fall", "USA")
banana = Fruit("Banana", "Yellow", "Sweet", 120, 0.5, "Year-round", "Ecuador")
orange = Fruit("Orange", "Orange", "Citrus", 130, 0.8, "Winter", "Spain")
grape = Fruit("Grape", "Purple", "Sweet", 50, 2.0, "Summer", "Italy")
mango = Fruit("Mango", "Yellow", "Sweet", 200, 1.5, "Summer", "India")
kiwi = Fruit("Kiwi", "Brown", "Tart", 75, 1.0, "Winter", "New Zealand")
pineapple = Fruit("Pineapple", "Brown", "Sweet", 900, 3.0, "Year-round", "Costa Rica")



#2.Creating a Student Class
class Student:
    def __init__(self, name, age, grade, student_id, major, gpa, university):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
        self.university = university

# Creating objects for the Student class
student1 = Student("Akello", 20, "Second Year", "S123", "Computer Science", 3.8, "Makerere University")
student2 = Student("Byamugisha", 21, "Third Year", "S456", "Electrical Engineering", 3.5, "Kyambogo University")
student3 = Student("Canowira", 22, "Fourth Year", "S789", "Medicine", 3.9, "Mbarara University")
student4 = Student("Ddumba", 19, "First Year", "S101", "Business Management", 3.6, "Victoria University")
student5 = Student("Egesa", 20, "Second Year", "S102", "Land Economics", 3.7, "Makerere University")
student6 = Student("Guma", 21, "Third Year", "S103", "Law", 3.4, "Uganda Christian University")
student7 = Student("Hassan", 22, "Fourth Year", "S104", "Architecture", 3.8, "Uganda Martyrs University")



#3.Creating a RugbyTeam Class
class RugbyTeam:
    def __init__(self, team_name, coach, captain, home_ground, league_titles_won, year_founded, team_color):
        self.team_name = team_name
        self.coach = coach
        self.players = captain
        self.home_ground = home_ground
        self.championships_won = league_titles_won
        self.year_founded = year_founded
        self.team_color = team_color
        
# Creating objects for the RugbyTeam class
team1 = RugbyTeam("Kampala Rhinos", "Marshall", "Shema", "Kampala Rugby Club", 0, 1990, "Yellow and Black")
team2 = RugbyTeam("Entebbe Mongers", "Makalama", "Odura", "Entebbe Rugby Club", 0, 1995, "Red and Black")
team3 = RugbyTeam("Jinja Hippos", "Quaresma", "Fahad", "Dam Waters Rugby Club", 2, 2000, "White and Gold")
team4 = RugbyTeam("KCB KOBS", "Mudhoola", "Ssempeke", "Kampala Rugby Club", 10, 1985, "Blue and White")
team5 = RugbyTeam("Gulu Warriors", "Okello", "Acen", "Gulu Rugby Club", 1, 2010, "Orange and Grey")
team6 = RugbyTeam("Mbale Eagles", "Byamugisha", "Ankunda", "Mbale Rugby Club", 0, 2015, "Purple and Gold")
team7 = RugbyTeam("Fort Portal Falcons", "Akiiki", "Adyeri", "Fort Portal Rugby Club", 2, 2018, "Teal and White")



#4.Creating a MobilePhone class
class MobilePhone:
    def __init__(self, brand, model, storage, ram, battery, price, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.ram = ram
        self.battery = battery
        self.price = price
        self.color = color

#Creating objects for the MobilePhone class
phone1 = MobilePhone("Samsung", "Galaxy S21", "128GB", "8GB", "4000mAh", 799, "Phantom Gray")
phone2 = MobilePhone("Apple", "iPhone 13", "256GB", "6GB", "3095mAh", 999, "Midnight")
phone3 = MobilePhone("Google", "Pixel 6", "128GB", "8GB", "4614mAh", 599, "Stormy Black")
phone4 = MobilePhone("OnePlus", "9 Pro", "256GB", "12GB", "4500mAh", 969, "Morning Mist")
phone5 = MobilePhone("Xiaomi", "Mi 11", "256GB", "8GB", "4600mAh", 749, "Horizon Blue")
phone6 = MobilePhone("Sony", "Xperia 5", "128GB", "8GB", "4500mAh", 899, "Black")
phone7 = MobilePhone("Nokia", "8.3", "128GB", "8GB", "4500mAh", 699, "Polar Night")



#5.Creating a Music class
class Music:
    def __init__(self, title, artist, album, genre, duration, release_year, studio):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration = duration
        self.release_year = release_year
        self.studio = studio

#Creating objects for the Music Class
music1 = Music("Shape of You", "Ed Sheeran", "Divide", "Pop", "3:53", 2017, "Asylum Records")
music2 = Music("Blinding Lights", "The Weeknd", "After Hours", "Synthwave", "3:20", 2019, "XO Records")
music3 = Music("Levitating", "Dua Lipa", "Future Nostalgia", "Disco", "3:23", 2020, "Warner Records")
music4 = Music("Peaches", "Justin Bieber", "Justice", "R&B", "3:18", 2021, "Def Jam Recordings")
music5 = Music("Good 4 U", "Olivia Rodrigo", "SOUR", "Pop Punk", "2:58", 2021, "Geffen Records")
music6 = Music("Stay", "The Kid LAROI & Justin Bieber", "F*CK LOVE 3", "Pop", "3:22", 2021, "Columbia Records")
music7 = Music("Industry Baby", "Lil Nas X & Jack Harlow", "Montero", "Hip Hop", "3:29", 2021, "Columbia Records")



#6.Creating a Movies class
class Movies:
    def __init__(self, title, director, genre, duration, release_year, studio, rating):
        self.title = title
        self.director = director
        self.genre = genre
        self.duration = duration
        self.release_year = release_year
        self.studio = studio
        self.rating = rating

#Creating objects for the Movies class
movie1 = Movies("Inception", "Christopher Nolan", "Sci-Fi", "2h 28m", 2010, "Warner Bros.", 8.8)
movie2 = Movies("The Godfather", "Francis Ford Coppola", "Crime", "2h 55m", 1972, "Paramount Pictures", 9.2)
movie3 = Movies("Pulp Fiction", "Quentin Tarantino", "Crime", "2h 34m", 1994, "Miramax", 8.9)
movie4 = Movies("The Dark Knight", "Christopher Nolan", "Action", "2h 32m", 2008, "Warner Bros.", 9.0)
movie5 = Movies("Forrest Gump", "Robert Zemeckis", "Drama", "2h 22m", 1994, "Paramount Pictures", 8.8)
movie6 = Movies("The Shawshank Redemption", "Frank Darabont", "Drama", "2h 22m", 1994, "Castle Rock Entertainment", 9.3)
movie7 = Movies("The Matrix", "Lana Wachowski", "Sci-Fi", "2h 16m", 1999, "Warner Bros.", 8.7)



#7.Creating a Countries class
class Countries:
    def __init__(self, name, capital, population, area, language, currency, president):
        self.name = name
        self.capital = capital
        self.population = population
        self.area = area
        self.language = language
        self.currency = currency
        self.president = president
        
country1 = Countries("Uganda", "Kampala", 45741007, 241038, "English", "Ugandan Shilling", "Yoweri Museveni")
country2 = Countries("Kenya", "Nairobi", 53771296, 580367, "Swahili", "Kenyan Shilling", "William Ruto")
country3 = Countries("Tanzania", "Dodoma", 59734218, 945087, "Swahili", "Tanzanian Shilling", "Samia Suluhu Hassan")
country4 = Countries("Rwanda", "Kigali", 12952218, 26338, "Kinyarwanda", "Rwandan Franc", "Paul Kagame")
country5 = Countries("Burundi", "Gitega", 11890784, 27834, "Kirundi", "Burundian Franc", "Évariste Ndayishimiye")
country6 = Countries("South Sudan", "Juba", 10975920, 619745, "English", "South Sudanese Pound", "Salva Kiir Mayardit")
country7 = Countries("Somalia", "Mogadishu", 15893222, 637657, "Somali", "Somali Shilling", "Hassan Sheikh Mohamud")



#8.Creating a EPLClub class
class EPLClub:
    def __init__(self, name, manager, stadium, capacity, established, owner, league_titles):
        self.name = name
        self.manager = manager
        self.stadium = stadium
        self.capacity = capacity
        self.established = established
        self.owner = owner
        self.league_titles = league_titles

club1 = EPLClub("Manchester United", "Ruben Amorin", "Old Trafford", 74879, 1878, "Glazer Family", 20)
club2 = EPLClub("Liverpool", "Arne Slot", "Anfield", 53394, 1892, "Fenway Sports Group", 20)
club3 = EPLClub("Chelsea", "Enzo Maresca", "Stamford Bridge", 40834, 1905, "Todd Boehly", 6)
club4 = EPLClub("Arsenal", "Mikel Arteta", "Emirates Stadium", 60260, 1886, "Stan Kroenke", 13)
club5 = EPLClub("Tottenham Hotspur", "Thomas Frank", "Tottenham Hotspur Stadium", 62850, 2019, "ENIC Group", 2)
club6 = EPLClub("Manchester City", "Pep Guardiola", "Etihad Stadium", 55017, 1880, "City Football Group", 9)
club7 = EPLClub("Leicester City", "Marti Cifuentes", "King Power Stadium", 32312, 1884, "King Power International", 1)
