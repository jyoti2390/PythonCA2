import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { FundService } from '../services/fund.service';
import { Fund } from '../model/fund';

@Component({
  selector: 'app-hfund',
  templateUrl: './hfund.component.html',
  styleUrls: ['./hfund.component.css']
})
export class HFundComponent implements OnInit {

  fund: Fund;
  constructor(public fundService: FundService, public router: Router) {
    this.fund = new Fund;
  }

  findByFhTotal(fhTotal: number) {
    this.fundService.getByReturn(fhTotal);

  }

  findByAum(fundAum: number) {
    this.fundService.getByAum(fundAum);
  }

  findByAmc(fundAmc: string) {
    this.fundService.getAllByFundAmc(fundAmc);
  }

  findByRisk(fundRisk: string) {
    this.fundService.getAllByFundRisk(fundRisk);
  }

  fundsAll() {
    this.fundService.getFunds();

  }

  orderByFundName() {
    this.fundService.orderbyFundName();
  }

  orderByFundAum() {
    this.fundService.orderbyFundAum();
  }

  findById(fundId: number) {
    this.fundService.getByFundId(fundId);
  }

  searchFund(name: string) {
    this.fundService.getAllByFundAmc(name);
    this.router.navigateByUrl('/funds/' + name);
  }

  ngOnInit(): void {
    if (!this.fundService.searchFlag) {
      this.fundService.getFunds();

      this.fundService.getFundAmc();
      this.fundService.getFundRisk();
    }
  }
}
