-- Keep a log of any SQL queries you execute as you solve the mystery.

-- SELECT description FROM crime_scene_reports WHERE year = 2023 AND month = 7 AND day = 28 AND street = 'Humphrey Street';

-- SELECT name, transcript FROM interviews WHERE transcript like '%bakery%' AND  year = 2023 AND month = 7 AND day = 28;

-- SELECT * FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute <= 25 AND minute >= 15;

-- SELECT * FROM atm_transactions WHERE day =28 AND year =2023 AND month =7 AND atm_location ='Leggett Street' AND transaction_type ='withdraw';

-- SELECT * FROM phone_calls WHERE year =2023 AND month =7 AND day =28 AND duration < 60;

-- SELECT * FROM passengers WHERE flight_id =
-- (SELECT id FROM flights WHERE year = 2023 AND month = 7 AND day = 29 AND origin_airport_id =
-- (SELECT id FROM airports WHERE city ='Fiftyville') ORDER BY hour,minute LIMIT 1);

-- ANSWER to first question thief's name = Bruce
SELECT name FROM people WHERE license_plate in
(SELECT license_plate FROM bakery_security_logs WHERE year = 2023 AND month = 7 AND day = 28 AND hour = 10 AND minute <= 25 AND minute >= 15)
AND passport_number in
(SELECT passport_number FROM passengers WHERE flight_id =
(SELECT id FROM flights WHERE year = 2023 AND month = 7 AND day = 29 AND origin_airport_id =
(SELECT id FROM airports WHERE city ='Fiftyville') ORDER BY hour,minute LIMIT 1))
AND phone_number in
(SELECT caller FROM phone_calls WHERE year =2023 AND month =7 AND day =28 AND duration < 60)
AND people.id in
(SELECT person_id FROM bank_accounts WHERE account_number in
(SELECT account_number FROM atm_transactions WHERE day =28 AND year =2023 AND month =7 AND atm_location ='Leggett Street' AND transaction_type ='withdraw'));

-- ANSWER to second question city escaped to = Dallas
SELECT city FROM airports WHERE id =
(SELECT destination_airport_id FROM flights WHERE year = 2023 AND month = 7 AND day = 29 AND origin_airport_id =
(SELECT id FROM airports WHERE city ='Fiftyville') ORDER BY hour,minute LIMIT 1);

-- ANSWER to third question peorson who helped the thief = Robin
SELECT name FROM people WHERE phone_number =
(SELECT receiver  FROM phone_calls WHERE caller = '(367) 555-5533' AND year =2023 AND month =7 AND day =28 AND duration < 60);
