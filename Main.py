import random

class Grass:
    def __init__(self):
        self.amount = 400
        self.growth_rate = 5
        
    def grow(self):
        self.amount = min(400, self.amount + self.growth_rate)
        
    def is_available(self):
        return self.amount > 0
        
    def reduce(self):
        if self.is_available():
            self.amount -= 1
            return True
        return False

class Rabbit:
    def __init__(self):
        self.energy = 45  
        self.energy_loss = 3  
        self.age = 0
        self.stages_without_food = 0
        
    def is_alive(self):
        return (self.energy > 0 and self.age < 25 and 
                self.stages_without_food < 3)
        
    def eat_grass(self):
        self.energy = min(45, self.energy + 10)
        self.stages_without_food = 0
        
    def can_reproduce(self):
        return (self.age >= 10 and self.energy >= 40 and 
                random.random() < 0.5)
        
    def update(self):
        self.age += 1
        self.energy -= self.energy_loss
        if self.energy <= 0:
            self.stages_without_food += 1
        else:
            self.stages_without_food = 0
            
    def reproduce(self):
        if self.can_reproduce():
            self.energy -= 20 
            return Rabbit()
        return None

class Wolf:
    def __init__(self, energy=100, energy_loss=2):
        self.energy = energy  
        self.energy_loss = energy_loss 
        self.age = 0
        self.stages_without_food = 0
        
    def is_alive(self):
        return (self.energy > 0 and self.age < 50 and 
                self.stages_without_food < 2)
        
    def eat_rabbit(self):
        self.energy = min(200, self.energy + 10)
        self.stages_without_food = 0
        
    def can_reproduce(self):
        return (self.age >= 10 and self.energy >= 120 and 
                random.random() < 0.5)
        
    def update(self):
        self.age += 1
        self.energy -= self.energy_loss
        if self.energy <= 0:
            self.stages_without_food += 1
        else:
            self.stages_without_food = 0
            
    def reproduce(self):
        if self.can_reproduce():
            self.energy -= 60 
            return Wolf(energy=100, energy_loss=self.energy_loss)
        return None

class Ecosystem:
    def __init__(self):
        print("\nWolf Config")
        wolf_count = int(input("Wolf population (default = 2 units): ") or 2)
        wolf_energy = int(input("Wolf Energy (default = 100): ") or 100)
        wolf_energy_loss = int(input("Wolf Metabolism rate (default = 2): ") or 2)
        
        self.grass = Grass()
        self.rabbits = [Rabbit() for _ in range(20)]
        self.wolves = [Wolf(wolf_energy, wolf_energy_loss) for _ in range(wolf_count)]
        self.stage = 0

    def simulate_one_stage(self):
        self.stage += 1
        print(f"\n--- Stage {self.stage} ---")
        
        self.grass.grow()
        
        new_rabbits = []
        for rabbit in self.rabbits:
            if self.grass.is_available() and random.random() < 0.5:
                if self.grass.reduce():
                    rabbit.eat_grass()
            
            rabbit.update()
            
            if rabbit.can_reproduce():
                new_rabbit = rabbit.reproduce()
                if new_rabbit:
                    new_rabbits.append(new_rabbit)
                    
        self.rabbits.extend(new_rabbits)
        
        new_wolves = []
        for wolf in self.wolves:
            if self.rabbits and random.random() < 0.3:
                rabbit = random.choice(self.rabbits)
                self.rabbits.remove(rabbit)
                wolf.eat_rabbit()
            
            wolf.update()
            
            if wolf.can_reproduce():
                new_wolf = wolf.reproduce()
                if new_wolf:
                    new_wolves.append(new_wolf)
                    
        self.wolves.extend(new_wolves)
        
        self.rabbits = [r for r in self.rabbits if r.is_alive()]
        self.wolves = [w for w in self.wolves if w.is_alive()]
        
        self.show_status()
        
    def show_status(self):
        print(f"Stage: {self.stage}")
        print(f"Grass: {self.grass.amount}")
        print(f"Rabbits: {len(self.rabbits)}")
        for i, rabbit in enumerate(self.rabbits[:], 1):
            print(f"  Rabbit {i}: Age={rabbit.age}, Energy={rabbit.energy}")
            
        print(f"Wolves: {len(self.wolves)}")
        for i, wolf in enumerate(self.wolves, 1):
            print(f"  Wolf {i}: Age={wolf.age}, Energy={wolf.energy}")
        
    def is_simulation_complete(self):
        return len(self.rabbits) == 0 and len(self.wolves) == 0
        
    def run(self):
        while not self.is_simulation_complete():
            self.simulate_one_stage()
            input("Press Enter to see next stage...")

def main():
    eco = Ecosystem()
    eco.run()

if __name__ == "__main__":
    main()