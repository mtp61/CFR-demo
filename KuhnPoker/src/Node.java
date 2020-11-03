import java.util.Arrays;

public class Node {
	public String infoSet;
	public double[] regretSum = new double[Constants.NUM_ACTIONS];
	public double[] strategy = new double[Constants.NUM_ACTIONS];
	public double[] strategySum = new double[Constants.NUM_ACTIONS];
	
	// get current information set mixed strategy through regret-matching
	public double[] getStrategy(double realizationWeight) {
		double normalizingSum = 0;
		for (int a = 0; a < Constants.NUM_ACTIONS; a++) {
			strategy[a] = regretSum[a] > 0 ? regretSum[a] : 0;
			normalizingSum += strategy[a];
		}
		
		for (int a = 0; a < Constants.NUM_ACTIONS; a++) {
			if (normalizingSum > 0) {
				strategy[a] /= normalizingSum;
			} else {
				strategy[a] = 1.0 / Constants.NUM_ACTIONS;
				strategySum[a] += realizationWeight * strategy[a];
			}
		}
		
		return strategy;
	}
	
	// get average information set mixed strategy across all training iterations
	public double[] getAverageStrategy() {
		double[] avgStrategy = new double[Constants.NUM_ACTIONS];
		double normalizingSum = 0;
		//System.out.println(Arrays.toString(strategySum));
		for (int a = 0; a < Constants.NUM_ACTIONS; a++) {
			normalizingSum += strategySum[a];
		}
		
		for (int a = 0; a < Constants.NUM_ACTIONS; a++) {
			if (normalizingSum > 0) {
				avgStrategy[a] = strategySum[a] / normalizingSum;
			} else {
				avgStrategy[a] = 1.0 / Constants.NUM_ACTIONS;
			}
		}
		
		return avgStrategy;
	}
	
	// get information set string representation
	public String toString() {
		return String.format("%4s: %s", infoSet, Arrays.toString(getAverageStrategy()));
	}
}
