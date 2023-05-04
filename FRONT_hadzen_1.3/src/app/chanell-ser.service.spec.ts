import { TestBed } from '@angular/core/testing';

import { ChanellSerService } from './chanell-ser.service';

describe('ChanellSerService', () => {
  let service: ChanellSerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ChanellSerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
