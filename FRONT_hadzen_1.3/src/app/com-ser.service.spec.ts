import { TestBed } from '@angular/core/testing';

import { ComSerService } from './com-ser.service';

describe('ComSerService', () => {
  let service: ComSerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ComSerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
