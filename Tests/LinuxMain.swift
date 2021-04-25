import XCTest

import testOnJuTests

var tests = [XCTestCaseEntry]()
tests += testOnJuTests.allTests()
XCTMain(tests)
