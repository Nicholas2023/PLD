# AirBnB Clone :smile:

## Description

This is a command-line interface (CLI) implementation of a simplified version of AirBnB. It allows users to interact with the application by creating, updating and deleting objects such as users, places, bookings and more.

## Classes

This project utilizes the following classes:

|Classes| BaseModel | FileStorage | User | State | City | Amenity | Place | Review |
|:-----:|:---------:|:-----------:|:----:|:-----:|:----:|:-------:|:-----:|:------:|
| PUBLIC INSTANCE ATTRIBUTE | `id` `created_at` `updated_at` | | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel` | Inherits from `BaseModel`| Inherits from `BaseModel` | Inherits from `BaseModel` |
| PUBLIC INSTANCE METHODS | `save` `to_dict` | `all` `new` `save` `reload` | | | | | | |
| PUBLIC CLASS ATTRIBUTE | | | `email` `password` `first_name` `last_name` | `name` | `state_id` `name` | `name` | `city_id` `user_id` `name` `description` `number_rooms` `number_bathrooms` `max_guest` `price_by_night` `latitude` `longitude` `amenity_ids` | `place_id` `user_id` `text` |
| PRIVATE CLASS ATTRIBUTE | | `file_path` `objects` | | | | | | |

## Storage

The above classes are handles by the abstracted storage engine defined in the `FileStorage` class.
Every time the backend is initialized, AirBnB instantiates an instance of `FileStorage` called `storage`. The `storage` object is loaded/re-loaded from any class instances stored in the JSON file `file.json`. As class instance are created, updated, or deleted, the `storage` object is used to register corresponding changes in the `file.json`.


## Command Interpreter / Console

The command interpreter provides a way to interact with the AirBnB application through a CLI. Here's how you can start and use it:

### How to start

1. Clone the repository to your local machine:

```bash
git clone https://github.com/your_username/AirBnB_clone.git
```

2. Navigate to the project directory:

```bash
cd AirBnB_clone
```

3. Run the console.py file:
```bash
./console.py
```

### How to Use

The console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file `console.py` at the command line.

```bash
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF all count create destroy help quit show update

(hbnb)
$
```

Alternatively, to use the AirBnB console in interactive mode, run the file `console.py` by itself:

```bash
$ ./console.py
```
While running in interactive mode, the console displays a prompt for input:

```bash
$ ./console.py
(hbnb)
```

To quit the console, enter the command `quit` or input an EOF signal (`ctrl-D`)

```bash
$ ./console.py
(hbnb) quit
$
```

```bash
(hbnb) EOF
```

Once the command interpreter is running, you can use the following commands to interact with the application:

- **create**: Create a new object  instance

```bash
(hbnb) create User
```

- **show**: Display the details of a specific object

```bash
(hbnb) show User 12345
```

- **destroy**: Delete a specific object

```bash
(hbnb) destroy User 12345
```

- **update**: Update the attributes of a specific object

```bash
(hbnb) update User 1234 email "user@example.com"
```

- **all**: Display the details of all objects or all objects of a specific class

```bash
(hbnb) all
(hbnb) all User
```

- **quit** Exit the command interpreter

```bash
(hbnb) quit
```

### Examples

- Creating a new user:

```bash
(hbnb) create User
```

- Showing the details of a place:

```bash
(hbnb) show Place 98765
```

- Update the name of a city:

```bash
(hbnb) update City 54321 name "New City Name"
```

## Authors

The following individuals have contributed to the development of this project:

- `Nicholas Otieno Odhiambo`
- `Anna Wambui Muturi`

## Branches and Pull Requests

We encourage the use of brances and pull request for collaborative development. When working on new features or bug fixes, create a new branch for your changes and submit a pull request to merge your changes intop the main branch.

For more information on branching and pullrequest, please refer to the `Github documentation`.
