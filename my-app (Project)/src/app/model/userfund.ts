export class UserFund {
    ufId: number;
    userId: number;
    fundId: number;
    ufType: string;
    ufAmount:number;
    ufDate:String;
    fundName:String;
    fundAmc:String
    totalFund:number;
    constructor() {
      this.userId = 0;
      this.ufId = 0;
      this.fundId = 0;
      this.ufType = '';
      this.ufDate='';
      this.ufAmount=0;
      this.fundName=''
      this.fundAmc='';
      this.totalFund=0;
    }
  }