import { TestBed } from '@angular/core/testing';

import { UserfundService } from './userfund.service';

describe('UserfundService', () => {
  let service: UserfundService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(UserfundService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
