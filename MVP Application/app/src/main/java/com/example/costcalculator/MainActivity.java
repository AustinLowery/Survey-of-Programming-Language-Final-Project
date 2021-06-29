package com.example.costcalculator;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    EditText mealCost, taxCost, tipCost;

    // view
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mealCost = findViewById(R.id.mealET);
        taxCost = findViewById(R.id.taxET);
        tipCost = findViewById(R.id.tipET);

        Presenter pres = new Presenter();

        findViewById(R.id.calculateButton).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                pres.startCalc(); // the call to the presenter
            }
        });
    }

    class CostViewData {
        String name;
        public CostViewData(String name){
            this.name = name;
        }
    }

    // model
    class CostCalculatorValues {
        float cost;
        float tax;
        float tip;

        public CostCalculatorValues(String c, String tx, String tp){
            this.cost = Float.valueOf(c);
            this.tax = Float.valueOf(tx);
            this.tip = Float.valueOf(tp);
        }
    }

    // presenter
    class Presenter {

        CostCalculatorValues ccv;
        public CostViewData cvd;

        public Presenter() {
            this.cvd = new CostViewData("Meal Cost Calculator");
            setupName();
        }

        private void startCalc(){
            ccv = new CostCalculatorValues(mealCost.getText().toString(), taxCost.getText().toString(),
                    tipCost.getText().toString());
            CostCalculator cc = new CostCalculator();
            cc.finalResult(ccv);
        }

        private void setupName(){
            setTitle(cvd.name);
        }
    }

    // talker
    class CostCalculator {
        TextView resultText = findViewById(R.id.resultTV);

        public void finalResult(CostCalculatorValues ccv){
            resultText.setText(String.valueOf(Math.round(
                    (ccv.cost * (1 + ccv.tax) + ccv.tip)*100.0
            )/100.0));
        }
    }

}