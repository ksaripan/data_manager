# Changelog

## 0.0.8
### Fix
- Handle invalid value for date/datetime field. Ex. 99999999

## 0.0.7
### Add
- Support decimal data field with all zero. Ex. 0000

## 0.0.6
### Add
- Support decimal data field with leading zero. Ex. 00-49.00

## 0.0.5
### Add
- Support decimal field without "." Ex. 1000 with decimal places = 2, then the result should be 10.00

## 0.0.4
### Fix
- Fix Integer field convert fix value to null

## 0.0.3
### Add
- Support AbstractReader can now change model

## 0.0.2
### Add
- Support comma separate number

## 0.0.1
### Add
- Support csv(comma, pipe)
- Support fix-width
