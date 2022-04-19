import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HFundComponent } from './hfund.component';

describe('HFundComponent', () => {
  let component: HFundComponent;
  let fixture: ComponentFixture<HFundComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HFundComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HFundComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
