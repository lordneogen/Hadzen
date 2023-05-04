import { TestBed } from '@angular/core/testing';

import { SubsSerService } from './subs-ser.service';

describe('SubsSerService', () => {
  let service: SubsSerService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SubsSerService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
