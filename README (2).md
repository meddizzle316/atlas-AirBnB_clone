
# AirBnb Console Project

This project is the first step in a series of interconnected projects, all designed to create an AirBnb clone. There are 2 main parts: the Console(our "Frontend"), the FileStorage class and the OOP framework with BaseModel as the parent class, both of which comprise our "Backend". This simple concole interface runs the simple commands "show, update, create, all" (along with some basic utility commands like "quit") that allows users to create instances of objects from the following classes (BaseModel, User, City, State, Place, Amenity, Review, more detailed view below). These objects are then converted to a dictionary and then dumped (converted to json format) into 'file.json'


## Classes Currently Available to Use

| Class | Attributes     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `BaseModel`      | `id, updated_at, created_at` | Base Class -- all classes inherit from BaseModel (all classes have id, updated_at and created_at attributes) |
| `User`      | `email, password, first_name, last_name` | User class -- contains information related to User |
| `State`      | `name, id` | State class -- contains information related to State |
| `City`      | `state_id, name` | City class -- contains information related to City|
| `Amentiy`      | `name` | Amenity class -- contains information related to Amenity |
| `Review`      | `place_id, user_id, text` | Review class -- contains information related to Reviews |
| `Place`      | `city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude, amenity_ids` | information related to Place |

## Usage/Examples

### Install

#### Interactive Mode:

git clone https://github.com/meddizzle316/atlas-AirBnB_clone.git

cd atlas-AirBnB_clone

./console


#### Non-Interative mode:

git clone https://github.com/meddizzle316/atlas-AirBnB_clone.git

cd atlas-AirBnB_clone

echo "command" | ./console


Below is a list of currently available commands. Be aware all commands are case sensitive

### Create

Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id

```create <class_name>``` 

```create BaseModel #output: <new BaseModel id>```

If the class name is missing or doesn't exist, create prints "** class name missing **" or ** class doesn't exist ** respectively

```create #output: ** class name missing **```

```create MyModel #output: ** class doesn't exist **```

### Show

Prints the string representation of an instance based on the class name and id

```show <class_name> <id>``` 

```show BaseModel 1111-1111-1111-1111 #output: <string representation of BaseModel.1111-1111-1111-1111```

If the class name is missing or doesn't exist, show prints "** class name missing **" or ** class doesn't exist ** respectively

```show #output: ** class name missing **```

```show MyModel #output: ** class doesn't exist **```

It additionally prints " instance id missing " if id is not included and " no instance found " if the id cannot be found

```show BaseModel #output:** instance id missing **```

```show BaseModel 2222-2222-2222-2222 #output: ** no instance found **```

### Destroy

Deletes an instance based on the class name and id

```destroy <class_name> <id>``` 

```destroy BaseModel 1111-1111-1111-1111```

```show BaseModel 1111-1111-1111-1111 #output: **instance id missing **```

If the class name is missing or doesn't exist, destroy prints "** class name missing **" or ** class doesn't exist ** respectively

```destroy #output: ** class name missing **```

```destory MyModel #output: ** class doesn't exist **```

It additionally prints " instance id missing " if id is not included and " no instance found " if the id cannot be found

```destroy BaseModel #output:** instance id missing **```

```destroy BaseModel 2222-2222-2222-2222 #output: ** no instance found **```

### All

Prints all string representation of all instances based or not on the class name
```all <class_name>``` 

```all BaseModel #output: <string representation of all BaseModel's in json>``` 

If the class name is missing or doesn't exist, all prints ** class doesn't exist ** 

```all #output: ** class doesn't exist **```

```all MyModel #output: ** class doesn't exist **```

### Update
Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)


```update <class_name> <id> <attribute_name> <attribute_value>```

```update BaseModel 1111-1111-1111-1111 new_attribute "attribute_value" ```

```all BaseModel #output: updated BaseModel with new_attribute``` 

If the class name is missing or doesn't exist, destroy prints "** class name missing **" or ** class doesn't exist ** respectively

```update #output: ** class name missing **```

```update MyModel #output: ** class doesn't exist **```

It additionally prints " instance id missing " if id is not included and "** no instance found **" if the id cannot be found

```update BaseModel #output:** instance id missing **```

```update BaseModel 2222-2222-2222-2222 #output: ** no instance found **```

It additionally prints " attribute missing " if attribute is not included and "** value missing **" if the attribute cannot be found

```update BaseModel 2222-2222-2222-2222 #output: ** attribute missing **``

```update BaseModel 2222-2222-2222-2222 attribute_name #output: ** value missing **``