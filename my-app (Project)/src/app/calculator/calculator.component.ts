var totalin=0;
var totalret=0;
import { Component, OnInit } from '@angular/core';
import { ChartType } from 'chart.js';
import { ChartOptions } from 'chart.js';
import { Label, monkeyPatchChartJsLegend, monkeyPatchChartJsTooltip, SingleDataSet } from 'ng2-charts';
@Component({
  selector: 'app-calculator',
  templateUrl: './calculator.component.html',
  styleUrls: ['./calculator.component.css']
})
export class CalculatorComponent implements OnInit {
  
  public totalInvestment:any
  totalValue:any
  totalreturn:any
  cal(val:any){
      this.totalInvestment=val.ia+val.mi*val.m;
      totalin=this.totalInvestment;
      this.totalreturn=val.ia+val.mi*Math.pow((1+(val.ar/100)/12),12)+this.totalInvestment
      totalret=this.totalreturn;

  }
  public pieChartOptions: ChartOptions = {
    responsive: true,
    
  };
  
  public pieChartLabels: Label[] = [['Invested Amount'], 'Return value'];
  
  public pieChartData: SingleDataSet = [10, 15];
  public pieChartType: ChartType = 'pie';
  public pieChartLegend = true;
  public pieChartPlugins = [];

  constructor() {
    monkeyPatchChartJsTooltip();
    monkeyPatchChartJsLegend();
  }

  ngOnInit(): void {
  }

}