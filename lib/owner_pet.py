class Pet:
    # Class variables
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        """Initialize a pet with name, pet_type, and optional owner."""
        # Validate pet_type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"pet_type must be one of {Pet.PET_TYPES}")
        
        # Validate owner if provided
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        
        # Add this instance to the all list
        Pet.all.append(self)


class Owner:
    """Owner class that can have multiple pets."""
    
    def __init__(self, name):
        """Initialize an owner with a name."""
        self.name = name
    
    def pets(self):
        """Return a full list of the owner's pets."""
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        """Add a pet to this owner, checking that pet is of type Pet."""
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self
    
    def get_sorted_pets(self):
        """Return a sorted list of pets by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)
    


# Example usage and testing:
if __name__ == "__main__":
    # Create owners
    alice = Owner("Alice")
    bob = Owner("Bob")
    
    # Create pets
    dog1 = Pet("Buddy", "dog", alice)
    cat1 = Pet("Whiskers", "cat", alice)
    bird1 = Pet("Tweety", "bird", bob)
    dog2 = Pet("Rex", "dog")  # No owner initially
    
    print("Testing basic functionality:")
    print(f"Alice's pets: {[pet.name for pet in alice.pets()]}")
    print(f"Bob's pets: {[pet.name for pet in bob.pets()]}")
    print()
    
    # Test add_pet method
    alice.add_pet(dog2)
    print(f"After adding Rex to Alice: {[pet.name for pet in alice.pets()]}")
    print()
    
    # Test sorted pets
    print(f"Alice's pets sorted: {[pet.name for pet in alice.get_sorted_pets()]}")
    print()
    
    # Test validation
    try:
        invalid_pet = Pet("Invalid", "unicorn")
    except Exception as e:
        print(f"Validation error for invalid pet_type: {e}")
    
    try:
        alice.add_pet("not a pet")
    except Exception as e:
        print(f"Validation error for add_pet: {e}")
    
    print(f"\nTotal pets created: {len(Pet.all)}")
    print(f"All pet types: {Pet.PET_TYPES}")