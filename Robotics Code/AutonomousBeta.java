/* Autonomous vs. 2_12_2017
 */
/*This is the code for autonomous operation of the robot that our FTC team built.
The code is based on the API from firstinspires.org. 
The robot started in different positions, and went in a combination of traveling to buttons and to the ramp, where the buttons
instructions utilised one light sensor for tracking to the buttons. Then one color sensor was utilised to determine the color of the buttons.
Once the color was determined, the robot would press the correct button. */
package org.firstinspires.ftc.teamcode;

import com.qualcomm.robotcore.eventloop.opmode.Autonomous;
import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.ftccommon.DbgLog;
import com.qualcomm.robotcore.eventloop.opmode.OpMode;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.Servo;
import com.qualcomm.robotcore.hardware.GyroSensor;
import com.qualcomm.robotcore.hardware.ColorSensor;
import com.qualcomm.robotcore.hardware.OpticalDistanceSensor;
import com.qualcomm.robotcore.hardware.TouchSensor;
import com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor;
import org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit;
import com.qualcomm.robotcore.hardware.HardwareMap;
import com.qualcomm.robotcore.util.Range;
import com.qualcomm.robotcore.util.ElapsedTime;



/*
 *
 * Autonomous operation employing LinearOpMode.
 * <p/>
 *
 *
 *
 */

@com.qualcomm.robotcore.eventloop.opmode.Autonomous(name="AutonomousBeta", group="Auto")
public class AutonomousBeta extends LinearOpMode {


    // Distance-to-Encoder scale: 560/L [deg/cm] Note: L = 6.283*WheelRadius.
    double DtoEScale = 17.5;

    // Power trim [-1 to 1]
    double rightPowerTrim = 0.0;
    double leftPowerTrim = 0.0;

    // Threshold and power Scale.
    double deadZoneThresh = 0.02;
    double powerScaleLo = 0.25;
    double powerScaleMid = 0.5;
    double powerScaleHi = 1.0;

    // Servo values:
    double BUTTONS_MIN_RANGE = 0.1;
    double BUTTONS_MAX_RANGE = 0.99;
    double BUTTONS_MID_RANGE = 0.5;
    double ARMS_MIN_RANGE = 0.1;
    double ARMS_MAX_RANGE = 0.65;
    double LORGBSERVO_MIN_RANGE = 0.1;
    double LORGBSERVO_MAX_RANGE = 0.5;


    //Servo Position
    double buttonSelectPosition;
    double armsPosition;
    double loRgbServoPosition;

    // Amount to change the button select servo position.
    double buttonSelectDelta = 0.025;
    double armsDelta = 0.025;
    double loRgbServoDelta = 0.025;


    // Motor and servo configuration:

    //Four motor drive:
    public DcMotor motorRightFront;
    public DcMotor motorLeftFront;
    public DcMotor motorRightBack;
    public DcMotor motorLeftBack;

    //Arm Drive
    public DcMotor motorArm;

    //Tilt motor:
    DcMotor motorTilt;

    //Button select servo:
    Servo buttonSelectServo;
    Servo leftArmServo;
    Servo rightArmServo;
    Servo loRgbServo;

    // Sensors:
    public GyroSensor sensorGyro;
    int xVal, yVal, zVal;
    int thetaVal;
    ColorSensor loSensorRGB;
    ColorSensor hiSensorRGB;
    ModernRoboticsI2cRangeSensor ultraSonicSensor;
    TouchSensor touchSensor_0;
    TouchSensor touchSensor_1;
    TouchSensor touchSensor_2;
    //TouchSensor touchSensor_3;

    ElapsedTime Timer;
    double timeOut;

    @Override
    public void runOpMode() throws InterruptedException {

        // Write device information (connection info, name and type) to the log file.
        hardwareMap.logDevices();

        /*
        * Use the hardwareMap to map sensors, dc motors, and servos by name.
        * Note that the names of the devices must match the names used in
        * configuration file.
        */

        // Four motor drive:
        motorLeftFront = hardwareMap.dcMotor.get("motor_2");
        motorLeftBack = hardwareMap.dcMotor.get("motor_4");
        motorRightFront = hardwareMap.dcMotor.get("motor_1");
        motorRightBack = hardwareMap.dcMotor.get("motor_3");
        motorLeftFront.setDirection(DcMotor.Direction.REVERSE);
        motorLeftBack.setDirection(DcMotor.Direction.REVERSE);
        motorLeftFront.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
        motorLeftBack.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
        motorRightFront.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
        motorRightBack.setMode(DcMotor.RunMode.RUN_USING_ENCODER);

        //Tilt motor:
        motorTilt = hardwareMap.dcMotor.get("motor_5");
        motorTilt.setMode(DcMotor.RunMode.RUN_USING_ENCODER);

	//Arms motors
        motorArm = hardwareMap.dcMotor.get("motor_6");
        motorArm.setMode(DcMotor.RunMode.RUN_USING_ENCODER);

        // Servo map:
        buttonSelectServo = hardwareMap.servo.get("servo_1");
	    leftArmServo = hardwareMap.servo.get("servo_2");
        rightArmServo = hardwareMap.servo.get("servo_3");
        loRgbServo = hardwareMap.servo.get("servo_4");

        // GyroSensor object:
        sensorGyro = hardwareMap.gyroSensor.get("Gyro");
        sensorGyro.calibrate();     // Calibrate gyro.

        // ColorSensor object.
        loSensorRGB = hardwareMap.colorSensor.get("LoRGB");
        loSensorRGB.enableLed(true);   // Turn the LED on (true) or off (false).

        // ColorSensor object.
        hiSensorRGB = hardwareMap.colorSensor.get("HiRGB");
        hiSensorRGB.enableLed(false);  // Turn the LED on (true) or off (false).

        // ultraSonicSensor object:
        ultraSonicSensor = hardwareMap.get(ModernRoboticsI2cRangeSensor.class, "USonic");

        // TouchSensor object:
        touchSensor_0 = hardwareMap.touchSensor.get("Touch_0");
        touchSensor_1 = hardwareMap.touchSensor.get("Touch_1");
        touchSensor_2 = hardwareMap.touchSensor.get("Touch_2");


        //touchSensor_3 = hardwareMap.touchSensor.get("Touch_3");

        boolean[] touchValue = getTouch();
        boolean touchValue_0 = false;
        boolean touchValue_1 = false;

        touchValue = getTouch();    //Sample touch sensors.
        touchValue_0 = touchValue[0];
        touchValue_1 = touchValue[1];

        // Assign servo starting position:
        buttonSelectPosition = BUTTONS_MID_RANGE;
	    armsPosition = ARMS_MIN_RANGE;
        loRgbServoPosition = 0.35;

        // Delay
        long waitTime = 100;    // wait time [ms]

        // Select game parameters:
        int gameColor = 0;
        int gameModality = 0;
        int gameAction = 0;
        int gameDelay = 0;
        int gameStart = 0;
        long gameDelayTime = 0;
        waitTime = 1000;

        while (gameColor == 0)
        {
            telemetry.addData("Red [B]", "");
            telemetry.addData("Blue [X]", "");
            telemetry.update();
            if (gamepad2.b) {
                gameColor = 1;          // Color Red.
                sleep(waitTime);
            }
            if (gamepad2.x) {
                gameColor = 2;          // Color Blue.
                sleep(waitTime);
            }
        }

        while (gameModality == 0)
        {
            telemetry.addData("Game Modality A: Buttons I [Y]", "");
            telemetry.addData("Game Modality B: Vortex [A]", "");
            telemetry.update();
            if (gamepad2.y) {
                gameModality = 1;       // Game Modality A.
                sleep(waitTime);
            }
            if (gamepad2.a) {
                gameModality = 2;       // Game Modality B.
                sleep(waitTime);
            }
        }

        if (gameModality == 1)
        {
            while (gameAction == 0) {
                telemetry.addData("Game Option A: Buttons II [B]", "");
                telemetry.addData("Not Available", "");
                telemetry.update();
                if (gamepad2.b) {
                    gameAction = 1;    // Game Option A.
                    sleep(waitTime);
                }
                if (gamepad2.x) {
                    gameAction = 1;    // Game Option B.
                    sleep(waitTime);
                }
            }
        }

        while (gameStart == 0) {
            telemetry.addData("Game Start A: Short [B]", "");
            telemetry.addData("Game Start B: Long [X]", "");
            telemetry.update();
            if (gamepad2.b) {
                gameStart = 1;      // Game Start A.
                sleep(waitTime);
            }
            if (gamepad2.x) {
                gameStart = 2;      // Game Start B.
                sleep(waitTime);
            }
        }

        while (gameDelay == 0) {
            telemetry.addData("Game Delay: 0 sec [A]", "");
            telemetry.addData("Game Delay: 10 sec [B]", "");
            telemetry.addData("Game Delay: 15 sec [X]", "");
            telemetry.update();
            if (gamepad2.a) {
                gameDelay = 1;      // Game Delay  [ms].
                gameDelayTime = 0;
                sleep(waitTime);
            }
            if (gamepad2.b) {
                gameDelay = 2;      // Game Delay [ms].
                gameDelayTime = 10000;
                sleep(waitTime);
            }
            if (gamepad2.x) {
                gameDelay = 3;      // Game Delay [ms].
                gameDelayTime = 15000;
                sleep(waitTime);
            }
        }

        while (!(gamepad2.y))
        {
            if (gameColor == 1) {
                telemetry.addData("Red", String.format("%01d", gameColor));
            } else if (gameColor == 2) {
                telemetry.addData("Blue", String.format("%01d", gameColor));
            } else {
                telemetry.addData("gameColor Error", String.format("%01d", gameColor));
            }
            if (gameModality == 1) {
                telemetry.addData("Game Modality A: Buttons I", String.format("%01d", gameModality));
            } else if (gameModality == 2) {
                telemetry.addData("Game Modality B: Vortex", String.format("%01d", gameModality));
            } else {
                telemetry.addData("gameModality Error", String.format("%01d", gameModality));
            }
            if (gameModality == 1) {
                if (gameAction == 1) {
                    telemetry.addData("Game Action A: Buttons II", String.format("%01d", gameAction));
                } else if (gameAction == 2) {
                    telemetry.addData("Game Action A: Park", String.format("%01d", gameAction));
                } else {
                    telemetry.addData("gameAction Error", String.format("%01d", gameAction));
                }
            }
            if (gameStart == 1) {
                telemetry.addData("Game Start: Short", String.format("%01d", gameStart));
            } else if (gameStart == 2) {
                telemetry.addData("Game Start: Long", String.format("%01d", gameStart));
            } else {
                telemetry.addData("gameStart Error", String.format("%01d", gameStart));
            }
            telemetry.addData("gameDelay:", String.format("%01d", gameDelay));
            telemetry.addData("Accept game settings [Y]", "");
            telemetry.update();
        }
        telemetry.addData("Game on !!", "");
        telemetry.update();

        // Initialize servos.
        buttonSelectServo.setPosition(buttonSelectPosition);
        rightArmServo.setPosition(armsPosition);
        leftArmServo.setPosition(1 - armsPosition);
        loRgbServo.setPosition(loRgbServoPosition);

        // Wait for the start button to be pressed.
        waitForStart();

        double distance = 0;            // Encoded drive distance [cm].
        double powerDistance = 0;       // Motor power [-1.0, 1.0].
        double theta = 0;               // GyroTurn -180 to 180 [deg].
        double powerTheta = 0;          // Motor power [-1.0, 1.0].
        double stallThreshEnc = 0;      // Encoder stall detect threshold.
        double stallThreshGyro = 0;     // Gyro stall detect threshold.
        boolean foundWhite = false;     // Color white found.
        double threshRange = 0;         // Range threshold [cm].
        boolean[] touchFlag = {false, false};
        waitTime = 100;

        int sequenceStep = 1;       // Step through sequence.
        int sequenceStepA = 1;      // Step through sequence.
        int sStep = 1;
        boolean sStepFlag = true;   // Step through flag.

        sleep(gameDelayTime);       // Delay start.

        if (gameModality == 1) {    //Game Modality A: Buttons.
            telemetry.addData("Start Game Modality A: Buttons", "");
            telemetry.update();
            while (opModeIsActive()) {
                switch (sequenceStep) {     // Step Game Modality A: Buttons.
                    case 1: // Move forwards.
                        if (gameStart == 1) {               // Short start.
                            if (gameColor == 1) {           // Red.
                                distance = 50;
                                powerDistance = 0.25;
                                theta = 0;
                                powerTheta = 0.05;
                            } else if (gameColor == 2) {    // Blue.
                                distance = 50;
                                powerDistance = 0.25;
                                theta = 0;
                                powerTheta = 0.05;
                            } else {
                                telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                telemetry.update();
                            }
                        } else if (gameStart == 2) {        // Long start.
                            if (gameColor == 1) {           // Red.
                                distance = 70;
                                powerDistance = 0.25;
                                theta = 0;
                                powerTheta = 0.05;
                            } else if (gameColor == 2) {    // Blue.
                                distance = 70;
                                powerDistance = 0.25;
                                theta = 0;
                                powerTheta = 0.05;
                            } else {
                                telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                telemetry.update();
                            }
                        } else {
                            telemetry.addData("gameStart Error", String.format("%01d", gameStart));
                            telemetry.update();
                        }
			            powerDistance = -powerDistance;
                        encodedDrive(powerDistance, distance, stallThreshEnc);
                        //gyroTurn(theta, powerTheta, powerTheta, stallThreshGyro);
                        sequenceStep++;
                        break;
                    case 2: // Turn and move forwards.
                        if (gameStart == 1) {               // Short start.
                            if (gameColor == 1) {           // Red.
                                distance = 90;
                                powerDistance = 0.25;
                                theta = -38;
                                powerTheta = 0.05;
                            } else if (gameColor == 2) {    // Blue.
                                distance = 90;
                                powerDistance = 0.25;
                                theta = 40;
                                powerTheta = 0.05;
                            } else {
                                telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                telemetry.update();
                            }
                        } else if (gameStart == 2) {        // Long start.
                            if (gameColor == 1) {           // Red.
                                distance = 150;
                                powerDistance = 0.25;
                                theta = -35;
                                powerTheta = 0.05;
                            } else if (gameColor == 2) {    // Blue.
                                distance = 150;
                                powerDistance = 0.25;
                                theta = 35;
                                powerTheta = 0.05;
                            } else {
                                telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                telemetry.update();
                            }
                        } else {
                            telemetry.addData("gameStart Error", String.format("%01d", gameStart));
                            telemetry.update();
                        }
                        gyroTurn(theta, powerTheta, powerTheta, stallThreshGyro);
			            powerDistance = -powerDistance;
                        encodedDrive(powerDistance, distance, stallThreshEnc);
                        sequenceStep++;
                        break;
                    case 3: // Slow down and move forward until white tape detected.
                        foundWhite = false;
                        distance = 50;
                        powerDistance = 0.05;
                        sleep(waitTime);
			            powerDistance = -powerDistance;
                        foundWhite = findLoRGBEncodedDrive(powerDistance, distance, stallThreshEnc);   // If the color is white.
                        if (foundWhite) {
                            telemetry.addData("White found", "");
                            telemetry.update();
                        } else {
                            telemetry.addData("White not found", "");
                            telemetry.update();
                        }
                        sleep(waitTime);
                        sequenceStep++;
                    case 4: // Turn towards buttons.
                        if (gameStart == 1) {               // Short start.
                            if (gameColor == 1) {           // Red.
                                distance = 3;
                                powerDistance = 0.05;
                                theta = -33;
                                powerTheta = 0.05;
                            } else if (gameColor == 2) {    // Blue.
                                distance = 3;
                                powerDistance = 0.05;
                                theta = 35;
                                powerTheta = 0.05;
                            } else {
                                telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                telemetry.update();
                            }
                        } else if (gameStart == 2) {        // Long start.
                            if (gameColor == 1) {           // Red.
                                distance = 0;
                                powerDistance = 0.25;
                                theta = -25;
                                powerTheta = 0.05;
                            } else if (gameColor == 2) {    // Blue.
                                distance = 0;
                                powerDistance = 0;
                                theta = 25;
                                powerTheta = 0.05;
                            } else {
                                telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                telemetry.update();
                            }
                        } else {
                            telemetry.addData("gameStart Error", String.format("%01d", gameStart));
                            telemetry.update();
                        }
                        powerDistance = -powerDistance;
                        encodedDrive(powerDistance, distance, stallThreshEnc);
                        gyroTurn(theta, powerTheta, powerTheta, stallThreshGyro);
                        sequenceStep++;
                        break;
                    case 5: // Line track to buttons.
                        powerDistance = 0.20;
                        threshRange = 17;
                        //lineTracker(threshRange, powerDistance);
                        powerDistance = -powerDistance;
                        sonarDrive(threshRange, powerDistance);
                        sequenceStep++;
                        break;
                    case 6: // Square to buttons.
                        timeOut = 1;
                        powerDistance = 0.05;
                        powerDistance = -powerDistance;
                        squareBot(timeOut, powerDistance);
                        powerDistance = 0.05;
                        powerDistance = -powerDistance;
                        distance = 6.5;
                        //encodedDrive(powerDistance, distance, stallThreshEnc);
                        sequenceStep++;
                        break;
                    case 7: // Select and press button.
                        if ((getHiRGB() == 1) || (getHiRGB() == 2)) {
                            if (getHiRGB() == gameColor) {
                                buttonSelectServo.setPosition(0.75);
                                sleep(5*waitTime);
                            } else {
                                buttonSelectServo.setPosition(0.25);
                                sleep(5*waitTime);
                            }
                            buttonSelectServo.setPosition(buttonSelectPosition);
                        } else {
                            telemetry.addData("Button color unresolved", "");
                            telemetry.update();
                        }
                        sequenceStep++;
                        break;
                    case 8: // Game Action A: Buttons I.
                        if (gameAction == 1) {      // Game Action A: Buttons II.
                            switch (sequenceStepA) {
                                case 1: // Back up and turn.
                                    if (gameStart == 1) {               // Short start.
                                        if (gameColor == 1) {           // Red.
                                            distance = 25;
                                            powerDistance = -0.1;
                                            theta = 81;
                                            powerTheta = 0.05;
                                        } else if (gameColor == 2) {    // Blue.
                                            distance = 25;
                                            powerDistance = -0.1;
                                            theta = -88;
                                            powerTheta = 0.05;
                                        } else {
                                            telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                            telemetry.update();
                                        }
                                    } else if (gameStart == 2) {        // Long start.
                                        if (gameColor == 1) {           // Red.
                                            distance = 25;
                                            powerDistance = -0.1;
                                            theta = 81;
                                            powerTheta = 0.05;
                                        } else if (gameColor == 2) {    // Blue.
                                            distance = 25;
                                            powerDistance = -0.1;
                                            theta = -88;
                                            powerTheta = 0.05;
                                        } else {
                                            telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                            telemetry.update();
                                        }
                                    } else {
                                        telemetry.addData("gameStart Error", String.format("%01d", gameStart));
                                        telemetry.update();
                                    }
				                    powerDistance = -powerDistance;
                                    encodedDrive(powerDistance, distance, stallThreshEnc);
                                    gyroTurn(theta, powerTheta, powerTheta, stallThreshGyro);
                                    sequenceStepA++;
                                    break;
                            case 2: // Drive towards Buttons II.
                                telemetry.addData("Sequence Step", sequenceStep);
                                telemetry.update();
                                if (gameStart == 1) {               // Short start.
                                    if (gameColor == 1) {           // Red.
                                        //distance = 110;
                                        powerDistance = 0.5;
                                        distance = 105;
                                        theta = 0;
                                        powerTheta = 0.05;
                                    } else if (gameColor == 2) {    // Blue.
                                        //distance = 110;
                                        //powerDistance = 0.5;
                                        distance = 110;
                                        powerDistance = 0.5;
                                        theta = 0;
                                        powerTheta = 0.05;
                                    } else {
                                        telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                        telemetry.update();
                                    }
                                } else if (gameStart == 2) {        // Long start.
                                    if (gameColor == 1) {           // Red.
                                        distance = 100;
                                        powerDistance = 0.5;
                                        theta = 0;
                                        powerTheta = 0.05;
                                    } else if (gameColor == 2) {    // Blue.
                                        distance = 100;
                                        powerDistance = 0.5;
                                        theta = 0;
                                        powerTheta = 0.05;
                                    } else {
                                        telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                        telemetry.update();
                                    }
                                } else {
                                    telemetry.addData("gameStart Error", String.format("%01d", gameStart));
                                    telemetry.update();
                                }
				                powerDistance = -powerDistance;
                                encodedDrive(powerDistance, distance, stallThreshEnc);
                                //gyroTurn(theta, powerTheta, powerTheta, stallThreshGyro);
                                sequenceStepA++;
                                break;
                            case 3: // Slow down and move forward until white tape detected.
                                foundWhite = true;
                                distance = 5;
                                powerDistance = 0.05;
                                sleep(waitTime);
				                powerDistance = -powerDistance;
                                //foundWhite = findLoRGBEncodedDrive(powerDistance, distance, stallThreshEnc);   // If the color is white.
                                if (foundWhite) {
                                    telemetry.addData("White found", "");
                                    telemetry.update();
                                } else {
                                    telemetry.addData("White not found", "");
                                    telemetry.update();
                                }
                                sleep(waitTime);
                                sequenceStepA++;
                                break;
                            case 4: // Turn towards buttons.
                                if (gameStart == 1) {               // Short start.
                                    if (gameColor == 1) {           // Red.
                                        distance = 6;
                                        powerDistance = 0.25;
                                        theta = -80;
                                        powerTheta = 0.05;
                                    } else if (gameColor == 2) {    // Blue.
                                        distance = 3;
                                        powerDistance = 0.25;
                                        theta = 87;
                                        powerTheta = 0.05;
                                    } else {
                                        telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                        telemetry.update();
                                    }
                                } else if (gameStart == 2) {        // Long start.
                                    if (gameColor == 1) {           // Red.
                                        distance = 0;
                                        powerDistance = 0.25;
                                        theta = -88;
                                        powerTheta = 0.05;
                                    } else if (gameColor == 2) {    // Blue.
                                        distance = 0;
                                        powerDistance = 0.25;
                                        theta = 88;
                                        powerTheta = 0.05;
                                    } else {
                                        telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                        telemetry.update();
                                    }
                                } else {
                                    telemetry.addData("gameStart Error", String.format("%01d", gameStart));
                                    telemetry.update();
                                }
                                powerDistance = -powerDistance;
                                encodedDrive(powerDistance, distance, stallThreshEnc);
                                gyroTurn(theta, powerTheta, powerTheta, stallThreshGyro);
                                //encodedDrive(powerDistance, distance, stallThreshEnc);
                                sequenceStepA++;
                                break;
                            case 5: // Line track to buttons.
                                powerDistance = 0.20;
                                threshRange = 15;
                                //lineTracker(threshRange, powerDistance);
                                powerDistance = -powerDistance;
                                sonarDrive(threshRange, powerDistance);
                                sequenceStepA++;
                                break;
                            case 6: // Square to buttons.
                                timeOut = 1;
                                powerDistance = 0.05;
                                powerDistance = -powerDistance;
                                squareBot(timeOut, powerDistance);
                                powerDistance = 0.05;
                                powerDistance = -powerDistance;
                                distance = 6;
                                //encodedDrive(powerDistance, distance, stallThreshEnc);
                                sequenceStepA++;
                                break;
                            case 7: // Select and press button.
                                if ((getHiRGB() == 1) || (getHiRGB() == 2)) {
                                    if (getHiRGB() == gameColor) {
                                        buttonSelectServo.setPosition(0.75);
                                        sleep(5*waitTime);
                                    } else {
                                        buttonSelectServo.setPosition(0.25);
                                        sleep(5*waitTime);
                                    }
                                    buttonSelectServo.setPosition(buttonSelectPosition);
                                } else {
                                    telemetry.addData("Button color unresolved", "");
                                    telemetry.update();
                                }
                                sequenceStepA++;
                                break;
                            default:
                                telemetry.addData("Game Action A: Buttons II", "");
                                telemetry.update();
                                break;
                        }
                    } else if (gameAction == 2) {   // Game Action A: Park.
                        switch (sequenceStepA) {
                            case 1: // Back up and turn.
                                if (gameStart == 1) {               // Short start.
                                    if (gameColor == 1) {           // Red.
                                        distance = 27;
                                        powerDistance = -0.1;
                                        theta = -82;
                                        powerTheta = 0.05;
                                    } else if (gameColor == 2) {    // Blue.
                                        distance = 27;
                                        powerDistance = -0.1;
                                        theta = 82;
                                        powerTheta = 0.05;
                                    } else {
                                        telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                        telemetry.update();
                                    }
                                } else if (gameStart == 2) {        // Long start.
                                    if (gameColor == 1) {           // Red.
                                        distance = 25;
                                        powerDistance = -0.1;
                                        theta = -82;
                                        powerTheta = 0.05;
                                    } else if (gameColor == 2) {    // Blue.
                                        distance = 25;
                                        powerDistance = -0.1;
                                        theta = 82;
                                        powerTheta = 0.05;
                                    } else {
                                        telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                        telemetry.update();
                                    }
                                } else {
                                    telemetry.addData("gameStart Error", String.format("%01d", gameStart));
                                    telemetry.update();
                                }
				                powerDistance = -powerDistance;
                                encodedDrive(powerDistance, distance, stallThreshEnc);
                                gyroTurn(theta, powerTheta, powerTheta, stallThreshGyro);
                                sequenceStepA++;
                                break;
                            case 2: // Drive towards ramp.
                                telemetry.addData("Sequence Step", sequenceStep);
                                telemetry.update();
                                if (gameStart == 1) {               // Short start.
                                    if (gameColor == 1) {           // Red.
                                        distance = 100;
                                        powerDistance = 0.5;
                                        theta = 0;
                                        powerTheta = 0.05;
                                    } else if (gameColor == 2) {    // Blue.
                                        distance = 100;
                                        powerDistance = 0.5;
                                        theta = 0;
                                        powerTheta = 0.05;
                                    } else {
                                        telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                        telemetry.update();
                                    }
                                } else if (gameStart == 2) {        // Long start.
                                    if (gameColor == 1) {           // Red.
                                        distance = 100;
                                        powerDistance = 0.5;
                                        theta = 0;
                                        powerTheta = 0.05;
                                    } else if (gameColor == 2) {    // Blue.
                                        distance = 100;
                                        powerDistance = 0.5;
                                        theta = 0;
                                        powerTheta = 0.05;
                                    } else {
                                        telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                        telemetry.update();
                                    }
                                } else {
                                    telemetry.addData("gameStart Error", String.format("%01d", gameStart));
                                    telemetry.update();
                                }
				                powerDistance = -powerDistance;
                                encodedDrive(powerDistance, distance, stallThreshEnc);
                                //gyroTurn(theta, powerTheta, powerTheta, stallThreshGyro);
                                sequenceStepA++;
                                break;
                            default:
                                telemetry.addData("Game Action A: Park", "");
                                telemetry.update();
                                break;
                        }
                    }   // Game Action A: Park.
                    default:
                        telemetry.addData("End Game Modality A: Buttons", "");
                        telemetry.update();
                        break;
                }   // Step Game Modality A: Buttons.
            }   // While opModeIsActive - Game Modality A.
        } else if (gameModality == 2) {     // Game Modality B: Vortex.
            telemetry.addData("Game Modality B: Vortex", "");
            telemetry.update();
            while (opModeIsActive()) {  // While opModeIsActive - Game Modality B.
                switch (sequenceStep) {
                    case 1: // Move forwards.
                        if (gameStart == 1) {               // Short start.
                            if (gameColor == 1) {           // Red.
                                distance = 50;
                                powerDistance = 0.25;
                                theta = 0;
                                powerTheta = 0.05;
                            } else if (gameColor == 2) {    // Blue.
                                distance = 50;
                                powerDistance = 0.25;
                                theta = 0;
                                powerTheta = 0.05;
                            } else {
                                telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                telemetry.update();
                            }
                        } else if (gameStart == 2) {        // Long start.
                            if (gameColor == 1) {           // Red.
                                distance = 70;
                                powerDistance = 0.25;
                                theta = 0;
                                powerTheta = 0.05;
                            } else if (gameColor == 2) {    // Blue.
                                distance = 70;
                                powerDistance = 0.25;
                                theta = 0;
                                powerTheta = 0.05;
                            } else {
                                telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                telemetry.update();
                            }
                        } else {
                            telemetry.addData("gameStart Error", String.format("%01d", gameStart));
                            telemetry.update();
                        }
			            powerDistance = -powerDistance;
                        encodedDrive(powerDistance, distance, stallThreshEnc);
                        //gyroTurn(theta, powerTheta, powerTheta, stallThreshGyro);
                        sequenceStep++;
                        break;
                    case 2: // Turn and align with ball.
                        if (gameStart == 1) {               // Short start.
                            if (gameColor == 1) {           // Red.
                                distance = 50;
                                powerDistance = 0.25;
                                theta = 45;
                                powerTheta = 0.05;
                            } else if (gameColor == 2) {    // Blue.
                                distance = 50;
                                powerDistance = 0.25;
                                theta = -45;
                                powerTheta = 0.05;
                            } else {
                                telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                telemetry.update();
                            }
                        } else if (gameStart == 2) {        // Long start.
                            if (gameColor == 1) {           // Red.
                                distance = 0;
                                powerDistance = 0.25;
                                theta = 0;
                                powerTheta = 0.05;
                            } else if (gameColor == 2) {    // Blue.
                                distance = 0;
                                powerDistance = 0.25;
                                theta = 0;
                                powerTheta = 0.05;
                            } else {
                                telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                telemetry.update();
                            }
                        } else {
                            telemetry.addData("gameStart Error", String.format("%01d", gameStart));
                            telemetry.update();
                        }
                        gyroTurn(theta, powerTheta, powerTheta, stallThreshGyro);
                        powerDistance = -powerDistance;
                        encodedDrive(powerDistance, distance, stallThreshEnc);
                        sequenceStep++;
                    case 3: // Turn and move forwards towards ball.
                        if (gameStart == 1) {               // Short start.
                            if (gameColor == 1) {           // Red.
                                distance = 50;
                                powerDistance = 0.25;
                                theta = -90;
                                powerTheta = 0.05;
                            } else if (gameColor == 2) {    // Blue.
                                distance = 50;
                                powerDistance = 0.25;
                                theta = 90;
                                powerTheta = 0.05;
                            } else {
                                telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                telemetry.update();
                            }
                        } else if (gameStart == 2) {        // Long start.
                            if (gameColor == 1) {           // Red.
                                distance = 50;
                                powerDistance = 0.25;
                                theta = 0;
                                powerTheta = 0.05;
                            } else if (gameColor == 2) {    // Blue.
                                distance = 50;
                                powerDistance = 0.25;
                                theta = 0;
                                powerTheta = 0.05;
                            } else {
                                telemetry.addData("Modality Color Error", String.format("%01d", gameColor));
                                telemetry.update();
                            }
                        } else {
                            telemetry.addData("gameStart Error", String.format("%01d", gameStart));
                            telemetry.update();
                        }
                        gyroTurn(theta, powerTheta, powerTheta, stallThreshGyro);
			            powerDistance = -powerDistance;
                        encodedDrive(powerDistance, distance, stallThreshEnc);
                        sequenceStep++;
                    default:
                        telemetry.addData("Game Modality B: Vortex", "");
                        telemetry.update();
                        break;
                }
            }   // While opModeIsActive - Game Modality B.

        } else {    // Game Modality B: Vortex.
            telemetry.addData("Modality Error", String.format("%01d", gameModality));
            telemetry.update();
        }           // gameModality.

        telemetry.addData("Autonomous Complete", "");
        telemetry.update();
    }     // runOpMode.


    // GyroTurn
    // TurnAngle is a + postive or negative angle in units of degrees; e.g., -180 to 180 [deg].
    // loPower and hiPower are positive numbers [0 - 1].
    // stallThreshGyro stall detect threshold.
    // For loPower = hiPower, GyroTurn will differentially power motor drives until robot
    // rotates TurnAngle degrees.
    // For loPower <> hiPower, the turn radius is given by RT = (WB/2)(vi+vo)/(vo-vi)
    //		WB = Wheel base
    //		vi = Inside wheel velocity (motor loPower)
    //		vo = Outside wheel velocity (motor speed)
    // Returns boolean stallDetect (motor stalled if true)
    public boolean gyroTurn(double turnAngle, double loPower, double hiPower, double stallThresh) throws InterruptedException {

        double rightPower = 0;
        double leftPower = 0;
        double turnSign = Math.signum(turnAngle);
        double turnAngleMag = Math.abs(turnAngle);
        double thetaVal = 0;
        boolean stallDetect = false;        // Stall detection.
        double currentPosition = 0;
        double changeInPosition = 0;
        double stallCount = stallThresh;    // Minimum stall counts/waitTime.
        long waitTime = 50;                 // Wait time [ms].

        int sequenceGyroStep = 1;        // Step through sequence.
        boolean sequenceGyroFlag = true;

        while (sequenceGyroFlag) {
            switch (sequenceGyroStep) {
                case 1:     // Calibrate the gyro.
                    //sensorGyro.calibrate();
                    //while (sensorGyro.isCalibrating()) {
                    //    Thread.sleep(waitTime);
                    //}
                    sensorGyro.resetZAxisIntegrator();      // Reset gyro.
                    sleep(waitTime);  // Delay [ms]
                    sequenceGyroStep++;
                    break;
                case 2:   // Configure right/left power.
                    if (Math.abs(loPower) == Math.abs(hiPower)) {       // Differential turn.
                        if (turnSign < 0) {
                            rightPower = Math.abs(hiPower);
                            leftPower = -rightPower;
                        } else {
                            leftPower = Math.abs(hiPower);
                            rightPower = -leftPower;
                        }
                    } else {                                            // Radius turn.
                        if (turnSign < 0) {
                            rightPower = Math.abs(hiPower);
                            leftPower = Math.abs(loPower);
                        } else {
                            leftPower = Math.abs(hiPower);
                            rightPower = Math.abs(loPower);
                        }
                    }
                    sequenceGyroStep++;
                    break;
                case 3:   // Reset encoder.
                    //motorRightFront.setMode(DcMotorController.RunMode.RESET_ENCODERS);
                    //motorRightBack.setMode(DcMotorController.RunMode.RESET_ENCODERS);
                    //motorLeftFront.setMode(DcMotorController.RunMode.RESET_ENCODERS);
                    //motorLeftBack.setMode(DcMotorController.RunMode.RESET_ENCODERS);
                    //motorRightFront.setMode(DcMotorController.RunMode.RUN_WITHOUT_ENCODERS);
                    //motorRightBack.setMode(DcMotorController.RunMode.RUN_WITHOUT_ENCODERS);
                    //motorLeftFront.setMode(DcMotorController.RunMode.RUN_WITHOUT_ENCODERS);
                    //motorLeftBack.setMode(DcMotorController.RunMode.RUN_WITHOUT_ENCODERS);
                    //motorRightFront.setMode(DcMotorController.RunMode.RUN_USING_ENCODERS);
                    //motorRightBack.setMode(DcMotorController.RunMode.RUN_USING_ENCODERS);
                    //motorLeftFront.setMode(DcMotorController.RunMode.RUN_USING_ENCODERS);
                    //motorLeftBack.setMode(DcMotorController.RunMode.RUN_USING_ENCODERS);
                    sequenceGyroStep++;
                    break;
                case 4:   // Initialize power setting.
                    rightPower = Range.clip(rightPower, -1, 1);
                    leftPower = Range.clip(leftPower, -1, 1);
                    sequenceGyroStep++;
                    break;
                case 5:   // Power motors.
                    motorRightFront.setPower(rightPower);
                    motorRightBack.setPower(rightPower);
                    motorLeftFront.setPower(leftPower);
                    motorLeftBack.setPower(leftPower);
                    sequenceGyroStep++;
                    break;
                case 6:   // Track turn angle.
                    thetaVal = 0;
                    while ((thetaVal < turnAngleMag) && (!stallDetect)) {
                        currentPosition = motorRightFront.getCurrentPosition();
                        sleep(waitTime);  // Delay [ms]
                        changeInPosition = Math.abs(currentPosition - motorRightFront.getCurrentPosition());
                        if (changeInPosition < stallCount) {
                            stallDetect = true;
                        }
                        thetaVal = 1.0*getThetaVal();
                        //telemetry.addData("Theta", String.format("%.2f", thetaVal));
                        //telemetry.addData("turnAngle", String.format("%.2f", turnAngleMag));
                        //telemetry.update();
                    }                    
                    motorRightFront.setPower(0);
                    motorRightBack.setPower(0);
                    motorLeftFront.setPower(0);
                    motorLeftBack.setPower(0);
                    sequenceGyroStep++;
                    break;
                default: // Report status.
                    if (stallDetect) {
                        telemetry.addData("Motor Stalled", String.valueOf(stallDetect));
                        telemetry.update();
                    }
                    sequenceGyroFlag = false;
                    break;
            }
        }
        return stallDetect;
    }


    // getThetaVal
    // Read thetaValue from gyro.
    // Returns thetaVal int {-180 to 180}
    public double getThetaVal() throws InterruptedException {

        int thetaVal = 0;

        // Get the angular rotation theta (heading) 0 - 360 deg.
        // Modern Robotics' gyro sensor keeps track of the current heading for the Z axis only.
        thetaVal = sensorGyro.getHeading();
        if (thetaVal > 180) {   // Change branch cut to +- 180
            thetaVal = thetaVal - 360;
        }
        return Math.abs(thetaVal);
    }


    // encodedDrive
    // Parameters power double {-1 to 1}, distance double in cm, stallThreshEnc stall detect threshold.
    // Returns boolean stallDetect (motor stalled if true)
    public boolean encodedDrive(double power, double distance, double stallThresh) throws InterruptedException {

        double rightPower = 0.0;
        double leftPower = 0.0;
        double encoderTarget = Math.abs(DtoEScale*distance);  // Encoder target value.
        double encoderOffset = 10000;
        boolean stallDetect = false;        // Stall detection.
        double currentPosition;
        double changeInPosition;
        double stallCount = stallThresh;    // Minimum stall counts/waitTime.
        long waitTime = 50;                 // wait time [ms]
        double rightPowerTrim = 0.0;        // Trim
        double leftPowerTrim = 0.0;         // Trim

        int sequenceEncoderStep = 1;        // Step through sequence.
        boolean sequenceEncoderFlag = true;

        //telemetry.addData("Connection: ", motorRight.getConnectionInfo());
        //telemetry.addData("Mode: ", motorRight.getMode());
        //telemetry.addData("Power: ", power);

        while (sequenceEncoderFlag) {
            switch (sequenceEncoderStep) {
                case 1:   // Reset encoder.
                    //motorRightFront.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                    //motorRightBack.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                    //motorLeftFront.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                    //motorLeftBack.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                    //motorRightFront.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                    //motorRightBack.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                    //motorLeftFront.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                    //motorLeftBack.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                    //encoderOffset = Math.abs(motorRightFront.getCurrentPosition());
                    encoderOffset = motorRightFront.getCurrentPosition();
                    sequenceEncoderStep++;
                    break;
                case 2:   // Initialize power setting.
                    rightPower = Range.clip(power + rightPowerTrim, -1, 1);
                    leftPower = Range.clip(power + leftPowerTrim, -1, 1);
                    sequenceEncoderStep++;
                    break;
                case 3:   // Set power.
                    motorRightFront.setPower(rightPower);
                    motorRightBack.setPower(rightPower);
                    motorLeftFront.setPower(leftPower);
                    motorLeftBack.setPower(leftPower);
                    sequenceEncoderStep++;
                    break;
                case 4:   // Track encoder position.
                    currentPosition = encoderOffset;
                    sleep(waitTime);  // Delay [ms]
                    while ((Math.abs(currentPosition - encoderOffset) < encoderTarget) && (!stallDetect)) {
                        sleep(waitTime);  // Delay [ms]
                        changeInPosition = Math.abs(currentPosition - motorRightFront.getCurrentPosition());
                        if (changeInPosition < stallCount) {
                            stallDetect = true;
                        }
                        sleep(waitTime);  // Delay [ms]
                        //currentPosition = Math.abs(motorRightFront.getCurrentPosition());
                        currentPosition = motorRightFront.getCurrentPosition();
                        //telemetry.addData("Current Position: ", String.format("%.2f", Math.abs(currentPosition - encoderOffset)));
                        //telemetry.addData("Encoder Target: ", String.format("%.2f", encoderTarget));
                        //telemetry.addData("Change In Position: ", String.format("%.2f", changeInPosition));
                        //telemetry.update();
                    }
                    motorRightFront.setPower(0);
                    motorRightBack.setPower(0);
                    motorLeftFront.setPower(0);
                    motorLeftBack.setPower(0);
                    sequenceEncoderStep++;
                    break;
                default: // Report status.
                    if (stallDetect) {
                        telemetry.addData("Motor Stalled: ", String.valueOf(stallDetect));
                        telemetry.update();
                    }
                    sequenceEncoderFlag = false;
                    break;
            }
        }
        return stallDetect;
    }


    // lineTracker
    // Line tracker employing Optical Distance or Ultrasound Range Sensor: stops
    // when getUSRange is true.
    // Parameters threshRange double [cm], motor power {-1 1}
    public void lineTracker(double threshRange, double power) throws InterruptedException {

        long waitTime = 10;             // wait time [ms]

        while (!getUSRange(threshRange)) {
            if (!getLoRGB()) {
                motorRightFront.setPower(0);
                motorRightBack.setPower(0);
                motorLeftFront.setPower(power);
                motorLeftBack.setPower(power);
                //sleep(waitTime);
            } else {
                motorRightFront.setPower(power);
                motorRightBack.setPower(power);
                motorLeftFront.setPower(0);
                motorLeftBack.setPower(0);
                //sleep(waitTime);
            }
        }
        motorRightFront.setPower(0);
        motorRightBack.setPower(0);
        motorLeftFront.setPower(0);
        motorLeftBack.setPower(0);
    }


    // sonarDrive
    // Drive employing Ultrasound Range Sensor: stops when getUSRange is true.
    // Parameters threshRange double [cm], motor power {-1 1}
    public void sonarDrive(double threshRange, double power) throws InterruptedException {

        while (!getUSRange(threshRange)) {
            motorRightFront.setPower(power);
            motorRightBack.setPower(power);
            motorLeftFront.setPower(power);
            motorLeftBack.setPower(power);
        }
        motorRightFront.setPower(0);
        motorRightBack.setPower(0);
        motorLeftFront.setPower(0);
        motorLeftBack.setPower(0);
    }


    // squareBot
    // Square robot with wall: stops when both touch sensors active or when timeOut is true.
    // Parameters threshRange double [cm], motor power {-1 1},
    public void squareBot(double timeOut, double power) throws InterruptedException {

        long waitTime = 100;             // wait time [ms].
        boolean[] touchFlag = {false, false};
        double getTimer = 0;

        //Timer.reset();

        touchFlag = getTouch();
        motorRightFront.setPower(power);
        motorRightBack.setPower(power);
        motorLeftFront.setPower(power);
        motorLeftBack.setPower(power);
        //while ((touchFlag[0] == false) || (touchFlag[1] == false) && (timeOut < getTimer)) {
        while ((touchFlag[0] == false) || (touchFlag[1] == false) ) {
            if (touchFlag[1] == true) {
                motorRightFront.setPower(0);
                motorRightBack.setPower(0);
            }
            else {
                motorRightFront.setPower(power);
                motorRightBack.setPower(power);
            }
            if (touchFlag[0] == true) {
                motorLeftFront.setPower(0);
                motorLeftBack.setPower(0);
            }
            else {
                motorLeftFront.setPower(power);
                motorLeftBack.setPower(power);
            }

            touchFlag = getTouch();
            //getTimer = Timer.time();
        }
        motorRightFront.setPower(0);
        motorRightBack.setPower(0);
        motorLeftFront.setPower(0);
        motorLeftBack.setPower(0);
    }


    // findLoRGBEncodedDrive (white)
    // Parameters power double {-1 to 1}, distance double in cm, stallThreshEnc stall detect threshold.
    // Returns boolean true if color found and !stallDetect (motor stalled).
    public boolean findLoRGBEncodedDrive(double power, double distance, double stallThresh) throws InterruptedException {

        double rightPower = 0.0;
        double leftPower = 0.0;
        double encoderTarget = Math.abs(DtoEScale*distance);  // Encoder target value.
        double encoderOffset = 10000;
        boolean stallDetect = false;        // Stall detection.
        boolean foundLoRGB = false;
        double currentPosition;
        double changeInPosition;
        double stallCount = stallThresh;    // Minimum stall counts/waitTime.
        long waitTime = 50;                 // wait time [ms].
        double rightPowerTrim = 0.0;        // Trim.
        double leftPowerTrim = 0.0;         // Trim.

        int sequenceEncoderStep = 1;        // Step through sequence.
        boolean sequenceEncoderFlag = true;

        //telemetry.addData("Connection: ", motorRight.getConnectionInfo());
        //telemetry.addData("Mode: ", motorRight.getMode());
        //telemetry.addData("Power: ", power);

        while (sequenceEncoderFlag) {
            switch (sequenceEncoderStep) {
                case 1:   // Reset encoder.
                    //motorRightFront.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                    //motorRightBack.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                    //motorLeftFront.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                    //motorLeftBack.setMode(DcMotor.RunMode.STOP_AND_RESET_ENCODER);
                    //motorRightFront.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                    //motorRightBack.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                    //motorLeftFront.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                    //motorLeftBack.setMode(DcMotor.RunMode.RUN_USING_ENCODER);
                    //encoderOffset = Math.abs(motorRightFront.getCurrentPosition());
                    encoderOffset = motorRightFront.getCurrentPosition();
                    sequenceEncoderStep++;
                    break;
                case 2:   // Initialize power setting.
                    rightPower = Range.clip(power + rightPowerTrim, -1, 1);
                    leftPower = Range.clip(power + leftPowerTrim, -1, 1);
                    sequenceEncoderStep++;
                    break;
                case 3:   // Set power.
                    motorRightFront.setPower(rightPower);
                    motorRightBack.setPower(rightPower);
                    motorLeftFront.setPower(leftPower);
                    motorLeftBack.setPower(leftPower);
                    sequenceEncoderStep++;
                    break;
                case 4:   // Track encoder position.
                    foundLoRGB = false;
                    currentPosition = encoderOffset;
                    sleep(waitTime);  // Delay [ms].
                    while ((Math.abs(currentPosition - encoderOffset) < encoderTarget)&& (!foundLoRGB) && (!stallDetect)) {
                        sleep(waitTime);  // Delay [ms].
                        changeInPosition = Math.abs(currentPosition - motorRightFront.getCurrentPosition());
                        if (changeInPosition < stallCount) {
                            stallDetect = true;
                        }
                        if (getLoRGB()) {
                            foundLoRGB = true;
                        }
                        sleep(waitTime);  // Delay [ms].
                        //currentPosition = Math.abs(motorRightFront.getCurrentPosition());
                        currentPosition = motorRightFront.getCurrentPosition();
                        //telemetry.addData("Current Position: ", String.format("%.2f", Math.abs(currentPosition - encoderOffset)));
                        //telemetry.addData("Encoder Target: ", String.format("%.2f", encoderTarget));
                        //telemetry.addData("Change In Position: ", String.format("%.2f", changeInPosition));
                        //telemetry.update();
                    }
                    motorRightFront.setPower(0);
                    motorRightBack.setPower(0);
                    motorLeftFront.setPower(0);
                    motorLeftBack.setPower(0);
                    sequenceEncoderStep++;
                    break;
                default: // Report status.
                    if (stallDetect) {
                        telemetry.addData("Motor Stalled: ", String.valueOf(stallDetect));
                        telemetry.update();
                    }
                    if (foundLoRGB) {
                        telemetry.addData("LoRGB Found: ", String.valueOf(foundLoRGB));
                        telemetry.update();
                    }
                    sequenceEncoderFlag = false;
                    break;
            }
        }
        return foundLoRGB;
    }


    // getLoLoRGB
    // Color Sensor: Returns boolean false = Unresolved, true = selectedColor.
    public boolean getLoRGB() throws InterruptedException {

        // Integer and normalized RGB values.
        boolean selectedColorFlag = false;
        double Thresh = 50;
        double nThresh = 0.29;
        double rValue = 0;
        double gValue = 0;
        double bValue = 0;
        double totalValue;
        double nRValue = 0;
        double nGValue = 0;
        double nBValue = 0;

        // Sample RGB values.
        rValue = loSensorRGB.red();
        gValue = loSensorRGB.green();
        bValue = loSensorRGB.blue();
        totalValue = rValue + gValue + bValue;

        // Normalized RGB.
        nRValue = rValue / totalValue;
        nGValue = gValue / totalValue;
        nBValue = bValue / totalValue;

        //Selected color = white.
        if ((totalValue > Thresh) && (nRValue >= nThresh) && (nGValue >= nThresh) && (nBValue >= nThresh)) {
            selectedColorFlag = true;
        } else {
            selectedColorFlag = false;
        }

        // Send information back to driver station using telemetry function.
        //telemetry.addData("Red  ", String.format("%.2f", rValue));
        //telemetry.addData("Green", String.format("%.2f", gValue));
        //telemetry.addData("Blue ", String.format("%.2f", bValue));
        //telemetry.addData("nRed  ", String.format("%.2f", nRValue));
        //telemetry.addData("nGreen", String.format("%.2f", nGValue));
        //telemetry.addData("nBlue ", String.format("%.2f", nBValue));
        //telemetry.addData("selectedColorFlag ", selectedColorFlag);
        //telemetry.update();

        return selectedColorFlag;
    }


    // getHiRGB
    // Color Sensor: Returns int 0 = Unresolved, 1 = Red, 2 = Blue.
    public int getHiRGB() throws InterruptedException {

        // Integer and normalized RGB values.
        boolean redFlag = false;
        boolean blueFlag = false;
        double rValue = 0;
        double gValue = 0;
        double bValue = 0;
        double totalValue;
        double nRValue = 0;
        double nGValue = 0;
        double nBValue = 0;
        int getRGB = 0;

        // Sample RGB values.
        rValue = hiSensorRGB.red();
        gValue = hiSensorRGB.green();
        bValue = hiSensorRGB.blue();
        totalValue = rValue + gValue + bValue + 1.0;

        // Normalized RGB.
        nRValue = rValue / totalValue;
        nGValue = gValue / totalValue;
        nBValue = bValue / totalValue;

        if (nBValue > nRValue) {
            blueFlag = true;
            redFlag = false;
            getRGB = 2;
        } else if (nBValue < nRValue) {
            blueFlag = false;
            redFlag = true;
            getRGB = 1;
        } else {
            blueFlag = false;
            redFlag = false;
            getRGB = 0;
        }

        // Send information back to driver station using telemetry function.
        //telemetry.addData("Red  ", rValue);
        //telemetry.addData("Green", gValue);
        //telemetry.addData("Blue ", bValue);
        //telemetry.addData("nRed  ", nRValue);
        //telemetry.addData("nGreen", nGValue);
        //telemetry.addData("nBlue ", nBValue);
        //telemetry.addData("Blue ", blueFlag);
        //telemetry.addData("Red ", redFlag);
        //telemetry.update();

        return getRGB;
    }

    // getUSRange
    // Ultrasonic Range Sensor: Returns boolean true = usRange > threshRange.
    // Parameter threshRange double {0-255 cm}.
    public boolean getUSRange(double threshRange) throws InterruptedException {


        double uSonicRange;      // Range value [0-255].
        boolean rangeReached = false;

        // Sample range.
        //uSonicRange = ultraSonicSensor.rawUltrasonic();   // Raw data.
        uSonicRange = ultraSonicSensor.getDistance(DistanceUnit.CM);

        if (uSonicRange < threshRange) {
            rangeReached = true;
        }

        //telemetry.addData("raw ultrasonic", uSonicRange);
        //telemetry.addData("cm", "%.2f cm", uSonicRange);
        //telemetry.update();

        return rangeReached;
    }


//    // getODSS
//    // Optical Distance Sensor: Returns boolean true = lightIntensity > threshODSS.
//    // Parameter threshODSS double {0-1}.
//    public boolean getODSS(double threshODSS) throws InterruptedException {
//
//        double lightIntensity;      // Normalized intensity value [0-1].
//        boolean proxReached = false;
//
//        // Sample intensity.
//        lightIntensity = oDSSensor.getLightDetected();
//        //lightIntensity = oDSSensor.getLightDetectedRaw();
//        if (lightIntensity > threshODSS) {
//            proxReached = true;
//        }
//
//        // Send information back to driver station using telemetry function.
//        //telemetry.addData("Intensity", lightIntensity);
//        //telemetry.addData("Threshold", threshODSS);
//        telemetry.addData("Proximity Reached ", proxReached);
//
//        return proxReached;
//    }

    // getTouch
    // Touch Sensor: Returns boolean true = pressed switch.
    public boolean[] getTouch() throws InterruptedException {

        boolean[] touchFlag = {false, false};
        double Value;

        touchFlag[0] = false;
        touchFlag[1] = false;

        // Sample sensors
        touchFlag[0] = touchSensor_0.isPressed();
        touchFlag[1] = touchSensor_1.isPressed();

        // Telemetry.
        //telemetry.addData("Touch Value", String.valueOf(touchFlag));
        //telemetry.addData("Touch 0", String.valueOf(touchFlag[0]));
        //telemetry.addData("Touch 1", String.valueOf(touchFlag[1]));
        //telemetry.update();

        return touchFlag;
    }

}       // Autonomous
