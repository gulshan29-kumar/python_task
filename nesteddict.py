#task 4
iiit_ranchi_structure = {
    "Visitor": {
        "Board of Governors": {
            "Finance Committee": {
                "Registrar": {
                    "Joint Registrar/Deputy Registrar": {
                        "Assistant Registrar": []
                    }
                },
                "Associate Dean Faculty Affairs": [],
                "Associate Dean Academic Affairs": {
                    "Examination Coordinator": []
                },
                "Associate Dean R&D": [],
                "Associate Dean Student Affairs": []
            },
            "Building & Works Committee": {},
            "Director": {
                "HOD - CSE/ECE/Sciences/Humanities and Management": {
                    "CSE": {
                        "Assistant Professors": ["Dr. A. Sharma", "Dr. B. Verma"]
                    },
                    "ECE": {
                        "Assistant Professors": ["Dr. C. Singh", "Dr. D. Kumar"]
                    },
                    "Humanities": {
                        "Assistant Professors": ["Dr. E. Gupta", "Dr. F. Yadav"]
                    }
                },
                "Chief Warden": {
                    "Hostel Warden": []
                },
                "FIC": [],
                "Coordinators - Training & Placement, Institute Website and Email Services, ERP": []
            },
            "Senate": {
                "Professor": {
                    "Associate Professor": {
                        "Assistant Professor": []
                    }
                }
            }
        }
    }
}

def search_assistant_professor(name, org_structure, current_path=""):
    for key, value in org_structure.items():
        new_path = f"{current_path} > {key}" if current_path else key
        
        if isinstance(value, dict):
            result = search_assistant_professor(name, value, new_path)
            if result:
                return result
        elif isinstance(value, list):
            if name in value:
                # Extract department from path
                path_parts = new_path.split(' > ')
                for dept in ["CSE", "ECE", "Humanities"]:
                    if dept in path_parts:
                        return dept
                return "Unknown Department"
    return None

# Example usage
prof_name = input("Enter the name of the Assistant Professor: ")

department = search_assistant_professor(prof_name, iiit_ranchi_structure)

if department:
    print(f"Assistant Professor '{prof_name}' belongs to the '{department}' department.")
else:
    print(f"Assistant Professor '{prof_name}' was not found in the structure.")