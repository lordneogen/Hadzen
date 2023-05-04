import { TestBed } from '@angular/core/testing';

import { MangSerService } from './mang-ser.service';

describe('MangSerService', () => {
  let service: MangSerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MangSerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
