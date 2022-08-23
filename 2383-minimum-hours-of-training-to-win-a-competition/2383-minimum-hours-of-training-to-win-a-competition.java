class _Solution {
    public int minNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        int training_hours = 0;
        int opponent_energy = 0;
        for (int i=0; i<energy.length; i++) {
            opponent_energy += energy[i];
        }
        if (initialEnergy > opponent_energy) {
            training_hours = 0;
        } else if (initialEnergy == opponent_energy) {
            training_hours++;
        } else {
            training_hours =  opponent_energy - initialEnergy + 1;
        }
        // System.out.println("The additional energy needed: " + training_hours);
        
        for (int i=0; i<experience.length; i++) {
            if (initialExperience > experience[i]) {
                initialExperience += experience[i];
            } else if (initialExperience == experience[i]) {
                training_hours++;
                initialExperience += experience[i] + 1;
            } else {
                training_hours += experience[i] - initialExperience + 1;
                initialExperience += experience[i];
            }
        }
        return training_hours;
    }
}

class Solution {
    public int minNumberOfHours(int initialEnergy, int initialExperience, int[] energy, int[] experience) {
        int currentEnergy = initialEnergy;
        int currentExperience = initialExperience;
        int result = 0;
        int diff = 0;
        for (int i = 0; i < energy.length; i++) {
            if (energy[i] >= currentEnergy) {   
                diff = energy[i] - currentEnergy + 1;
                result = result + diff;
                currentEnergy = currentEnergy + diff;
            }
            currentEnergy = currentEnergy - energy[i];
            if (experience[i] >= currentExperience) {
                diff = experience[i] - currentExperience + 1;
                result = result + diff;
                currentExperience = currentExperience + diff;
            }
            currentExperience = currentExperience + experience[i];
        }
        return result;
    }
}