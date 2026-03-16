"""
data/sample_data.py — Movie dataset for seeding the Endee 'movies' index.

Each item has an "embed_text" field that gets turned into a 384-dim vector,
plus rich metadata stored alongside it in Endee.
"""

MOVIES = [
    {
        "id": "mov_001",
        "embed_text": "A mind-bending sci-fi epic about astronauts travelling through a wormhole near Saturn to save humanity from extinction, exploring time dilation and love across dimensions.",
        "meta": {
            "title": "Interstellar",
            "year": 2014,
            "genre": ["Sci-Fi", "Drama"],
            "director": "Christopher Nolan",
            "rating": 8.7,
            "description": "A team of astronauts travel through a wormhole in search of a new home for humanity.",
        },
    },
    {
        "id": "mov_002",
        "embed_text": "A psychological thriller about a detective investigating a series of murders connected to the seven deadly sins in a dark, rainy city.",
        "meta": {
            "title": "Se7en",
            "year": 1995,
            "genre": ["Thriller", "Crime"],
            "director": "David Fincher",
            "rating": 8.6,
            "description": "Two detectives hunt a serial killer who uses the seven deadly sins as his modus operandi.",
        },
    },
    {
        "id": "mov_003",
        "embed_text": "A survival drama about a man stranded alone on a deserted island after a plane crash, using ingenuity and a volleyball as his only companion.",
        "meta": {
            "title": "Cast Away",
            "year": 2000,
            "genre": ["Drama", "Survival"],
            "director": "Robert Zemeckis",
            "rating": 7.8,
            "description": "A FedEx employee is stranded on a deserted island after his plane crashes.",
        },
    },
    {
        "id": "mov_004",
        "embed_text": "A time travel thriller where a man discovers he can send messages to the past, changing the present with unforeseen consequences.",
        "meta": {
            "title": "Frequency",
            "year": 2000,
            "genre": ["Sci-Fi", "Thriller"],
            "director": "Gregory Hoblit",
            "rating": 7.4,
            "description": "A man communicates with his deceased father through a time-warped radio.",
        },
    },
    {
        "id": "mov_005",
        "embed_text": "A dark fantasy film about a young girl who enters a mysterious labyrinth filled with creatures and moral choices during the aftermath of the Spanish Civil War.",
        "meta": {
            "title": "Pan's Labyrinth",
            "year": 2006,
            "genre": ["Fantasy", "Drama"],
            "director": "Guillermo del Toro",
            "rating": 8.2,
            "description": "A young girl discovers a fantasy world while living with her brutal stepfather in post-war Spain.",
        },
    },
    {
        "id": "mov_006",
        "embed_text": "An animated adventure about a young boy who befriends a giant robot from outer space during the Cold War and learns about sacrifice and heroism.",
        "meta": {
            "title": "The Iron Giant",
            "year": 1999,
            "genre": ["Animation", "Adventure"],
            "director": "Brad Bird",
            "rating": 8.1,
            "description": "A boy befriends a giant alien robot and protects him from government agents.",
        },
    },
    {
        "id": "mov_007",
        "embed_text": "A heist thriller where a crew of thieves use dream infiltration technology to plant an idea in a corporate executive's subconscious through layered dream worlds.",
        "meta": {
            "title": "Inception",
            "year": 2010,
            "genre": ["Sci-Fi", "Thriller"],
            "director": "Christopher Nolan",
            "rating": 8.8,
            "description": "A thief who steals corporate secrets through dream-sharing technology is given the task of planting an idea.",
        },
    },
    {
        "id": "mov_008",
        "embed_text": "A survival horror film where an astronaut is accidentally left on Mars and must use science and botany to survive until rescue.",
        "meta": {
            "title": "The Martian",
            "year": 2015,
            "genre": ["Sci-Fi", "Drama"],
            "director": "Ridley Scott",
            "rating": 8.0,
            "description": "An astronaut stranded on Mars must use his ingenuity to survive until a rescue mission arrives.",
        },
    },
    {
        "id": "mov_009",
        "embed_text": "A dark psychological thriller about a woman who goes missing on her wedding anniversary and her husband becomes the prime suspect while secrets unravel.",
        "meta": {
            "title": "Gone Girl",
            "year": 2014,
            "genre": ["Thriller", "Mystery"],
            "director": "David Fincher",
            "rating": 8.1,
            "description": "A wife's mysterious disappearance puts her husband under intense scrutiny.",
        },
    },
    {
        "id": "mov_010",
        "embed_text": "An epic wilderness survival story of a fur trapper who is mauled by a bear and left for dead, crawling through brutal winter landscapes seeking revenge.",
        "meta": {
            "title": "The Revenant",
            "year": 2015,
            "genre": ["Adventure", "Drama", "Survival"],
            "director": "Alejandro G. Iñárritu",
            "rating": 8.0,
            "description": "A frontiersman on a fur trading expedition fights for survival after being mauled by a bear.",
        },
    },
]
