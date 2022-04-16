import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Fund } from '../model/fund';





@Injectable({
  providedIn: 'root'
})
export class FundService {
  funds:Fund[];
  fundsAmc:string[];
  fundsRisk:string[];
  fundHistory:any;
  fundDetails:any;
  fundID:number;
  fundType:String;
  searchFlag: boolean

  constructor(public http: HttpClient) { 
    this.funds=[];
    this.fundsAmc=[];
    this.fundsRisk=[];
    this.fundHistory=[];
    this.fundID=0
    this.fundType=''
    this.searchFlag = false
  }

  getAllByFundAmc(fundAmc :string){
    this.http.get<Fund[]>('http://localhost:5000/funds/'+ fundAmc).subscribe((res)=>{
      this.funds = res;
      console.log(res)
    });
  }

  getAllByFundRisk(fundRisk :string){
    this.http.get<Fund[]>('http://localhost:5000/fundsRisk/'+ fundRisk).subscribe((res)=>{
      this.funds = res;
    });
  }

  searchByName(fundName :string){
    this.http.get<Fund[]>('http://localhost:5000/search/'+ fundName).subscribe((res)=>{
      this.funds = res;
      console.log(res)
    });
  }


  getByReturn(fhTotal :number){
    this.http.get<Fund[]>('http://localhost:5000/fundsReturn/'+ fhTotal).subscribe((res)=>{
      this.funds = res;
    });
  }

  getByAum(fundAum :number){
    this.http.get<Fund[]>('http://localhost:5000/fundsAum/'+ fundAum).subscribe((res)=>{
      this.funds = res;
      console.log(res)
    });
  }


  getFundAmc(){
    this.http.get<string[]>('http://localhost:5000/fundAmc').subscribe((res)=>{
      this.fundsAmc = res;
      
    });
  }
 
  orderbyFundName(){
    this.http.get<Fund[]>('http://localhost:5000/fundsOrder').subscribe((res)=>{
      this.funds = res;
    });
  }
  
  orderbyFundAum(){
    this.http.get<Fund[]>('http://localhost:5000/fundsOrderByAum').subscribe((res)=>{
      this.funds = res;
    });
  }

  getFundRisk(){
    this.http.get<string[]>('http://localhost:5000/fundRisk').subscribe((res)=>{
      this.fundsRisk = res;

    });
  }

  getFunds(){
    console.log("Hellow")
    this.http
      .get<any>('http://localhost:5000/funds/all')
      .subscribe((res) => {
        console.log(res)
        this.funds = res;
        console.log("jbhdhiguidhvbjhdvbw")
      });
  }


  getFundAndHistory(){
    this.http
      .get<Fund[]>('http://localhost:5000/funds/all/join')
      .subscribe((res) => {
        this.fundHistory = res;
        console.log(this.fundHistory)
      });
  }


  getByFundId(fundId :number){
    this.http.get<Fund[]>('http://localhost:5000/fundsById/'+ fundId).subscribe((res)=>{
      this.fundDetails = res;
      console.log(res)
      // this.fundID = this.fundDetails[12]
    });
  }

  

}