import { Component, OnInit } from '@angular/core';
import { FundService } from '../services/fund.service';

@Component({
  selector: 'app-detailfunds',
  templateUrl: './detailfunds.component.html',
  styleUrls: ['./detailfunds.component.css']
})
export class DetailfundsComponent implements OnInit {

  constructor(public fundService: FundService) { }


  findById(fundId: number){
    this.fundService.getByFundId(fundId);
  }

  ngOnInit(): void {
  }

}
