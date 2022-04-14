import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WhyvavjaComponent } from './whyvavja.component';

describe('WhyvavjaComponent', () => {
  let component: WhyvavjaComponent;
  let fixture: ComponentFixture<WhyvavjaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WhyvavjaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(WhyvavjaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
