/* TeleOp vs. 2_12_2017
 */
package org.firstinspires.ftc.teamcode;

import static java.lang.Math.*;  // Standard Math - Note Static

import com.qualcomm.robotcore.eventloop.opmode.Disabled;
import com.qualcomm.ftccommon.DbgLog;
import com.qualcomm.robotcore.eventloop.opmode.OpMode;
import com.qualcomm.robotcore.eventloop.opmode.LinearOpMode;
import com.qualcomm.robotcore.hardware.DcMotor;
import com.qualcomm.robotcore.hardware.Servo;
import com.qualcomm.robotcore.util.Range;
import com.qualcomm.robotcore.hardware.GyroSensor;
import com.qualcomm.robotcore.hardware.ColorSensor;
import com.qualcomm.robotcore.hardware.OpticalDistanceSensor;
import com.qualcomm.robotcore.hardware.TouchSensor;
import com.qualcomm.hardware.modernrobotics.ModernRoboticsI2cRangeSensor;
import org.firstinspires.ftc.robotcore.external.navigation.DistanceUnit;
import com.qualcomm.robotcore.hardware.HardwareMap;

/**
 * TeleOp operation employing OpMode.
 * <p/>
 * Manual control of the robot via gamepads 1 and 2.
 */

@com.qualcomm.robotcore.eventloop.opmode.TeleOp(name="TeleOpBeta", group="TOp")
public class TeleOpBeta extends OpMode {

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


    // Servo position:
    double buttonSelectPosition;
    double armsPosition;
    double loRgbServoPosition;

    // Amount to change servo position by.
    double buttonSelectDelta = 0.025;
    double armsDelta = 0.025;
    double loRgbServoDelta = 0.025;

    // Motor and servo configuration:

    //Four motor drive:
    DcMotor motorRightFront;
    DcMotor motorLeftFront;
    DcMotor motorRightBack;
    DcMotor motorLeftBack;

    //Tilt motor:
    DcMotor motorTilt;

    //Arms
    DcMotor motorArm;

    //Servo:
    Servo buttonSelectServo;
    Servo leftArmServo;
    Servo rightArmServo;
    Servo loRgbServo;

    // Sensors:
    public GyroSensor sensorGyro;
    ColorSensor loSensorRGB;
    ColorSensor hiSensorRGB;
    ModernRoboticsI2cRangeSensor ultraSonicSensor;
    TouchSensor touchSensor_0;
    TouchSensor touchSensor_1;
    TouchSensor touchSensor_2;
    //TouchSensor touchSensor_3;

    /**
     * Constructor
     */
    public TeleOpBeta() {

    }

    /*
     * Code to initialize run when the op mode is first enabled goes here:
     * 
     * @see com.qualcomm.robotcore.eventloop.opmode.OpMode#start()
     */
    @Override
    public void init() {
        /*
        * Use the hardwareMap to map sensors, dc motors, and servos by name.
        * Note that the names of the devices must match the names used in
        * configuration file.
        */

        //Four motor drive:
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
//        ultraSonicSensor = hardwareMap.get(ModernRoboticsI2cRangeSensor.class, "USonic");

        // OpticalDistanceSensor object:
        //oDSSensor = hardwareMap.opticalDistanceSensor.get("ODS");
        //oDSSensor.enableLed(true);     // Turn the LED on (true) or off (false).

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
        loRgbServoPosition = 0.5;

        // Initialize servos.
        buttonSelectServo.setPosition(buttonSelectPosition);
        rightArmServo.setPosition(armsPosition);
        leftArmServo.setPosition(1 - armsPosition);
        loRgbServo.setPosition(loRgbServoPosition);

    }

    // Code to run when the op mode is started:
    @Override public void start ()

    {
        //
        // Only actions that are common to all Op-Modes (i.e. both automatic and
        // manual) should be implemented here.
        //
        // This method is designed to be overridden.
        //

    } // start


    /*
     * This method will be called repeatedly in a loop.
     * 
     * @see com.qualcomm.robotcore.eventloop.opmode.OpMode#run()
     */
    @Override
    public void loop() {

        /*
         * Gamepad control.
         */

        // Tank drive.
        // Note that if y = -1 then joystick is pushed all of the way forward.
        float leftPower = -gamepad1.left_stick_y;
        float rightPower = -gamepad1.right_stick_y;

        //Arm drive.
        float armsPower = gamepad2.left_stick_y;

        //Tilt Drive
        float tiltPower = gamepad2.right_stick_y;

        //Clip Arm Values
        armsPower = Range.clip(armsPower, -1, 1);
        //Deadzone thresh check
        if (abs(armsPower) < deadZoneThresh || (touchSensor_2.isPressed() && armsPower <= 0)) {
            armsPower = 0;
        }
        //Clip Tilt Values
        tiltPower = Range.clip(tiltPower, -1, 1);
        //Deadzone thresh check
        if (abs(tiltPower) < deadZoneThresh) {
            tiltPower = 0;
        }

        // Clip the right/left values so that the values 
        // never exceed +/- 1.
        rightPower = Range.clip(rightPower, -1, 1);
        leftPower = Range.clip(leftPower, -1, 1);
        // Check for dead zone and scale speed.
        if (abs(rightPower) < deadZoneThresh) {
            rightPower = 0;
        }
        if (abs(leftPower) < deadZoneThresh) {
            leftPower = 0;
        }

        // Scale the joystick value using gamepad buttons Lo/Mid/Hi.
        if (gamepad1.right_bumper) {
            leftPower = (float) powerScaleMid * leftPower;
            rightPower = (float) powerScaleMid * rightPower;
        } else if (gamepad1.right_trigger > 0.25) {
            leftPower = (float) powerScaleHi * leftPower;
            rightPower = (float) powerScaleHi * rightPower;
        } else {
            leftPower = (float) powerScaleLo * leftPower;
            rightPower = (float) powerScaleLo * rightPower;
        }
        if(gamepad1.left_bumper) {
            leftPower = (float) -0.1;
            rightPower = (float) -0.1;
            boolean[] touchValue = getTouch();
            if(touchValue[1] == true) {
                rightPower = (float) 0.0;
            }
            if(touchValue[0] == true) {
                leftPower = (float) 0.0;
            }
        }

        // Scale the joystick value via remapping to make it easier to control
        // the robot more precisely at slower speeds.
        //rightPower = (float) scaleInput(rightPower);
        //leftPower = (float) scaleInput(leftPower);

        //Update motor drive:
        motorRightFront.setPower(rightPower);
        motorRightBack.setPower(rightPower);
        motorLeftFront.setPower(leftPower);
        motorLeftBack.setPower(leftPower);

        //Update arm drive:
        motorArm.setPower(armsPower);

        //Update tilt drive:
        motorTilt.setPower(tiltPower);

        // If the A button pressed, run trigger.
//        if(gamepad2.a)  {
//            sensorGyro.calibrate();     // Calibrate gyro.
//            encodedTrigger(0.1);
//        }

        // Buttons servo.
        if (gamepad2.dpad_left) {
            buttonSelectPosition += buttonSelectDelta;
        }
        else if (gamepad2.dpad_right) {
            buttonSelectPosition -= buttonSelectDelta;
        } else {
            buttonSelectPosition = BUTTONS_MID_RANGE;
        }

        // Clip the servo position values so range is not exceeded.
        buttonSelectPosition = Range.clip(buttonSelectPosition,
                BUTTONS_MIN_RANGE, BUTTONS_MAX_RANGE);

        // Set servo positions.
        buttonSelectServo.setPosition(buttonSelectPosition);
        if(gamepad2.x) {
            armsPosition += armsDelta;
        }
        else if(gamepad2.y){
            armsPosition -= armsDelta;
        }
        else {
        }
        armsPosition = Range.clip(armsPosition, ARMS_MIN_RANGE, ARMS_MAX_RANGE);
        rightArmServo.setPosition(armsPosition);
        leftArmServo.setPosition(1 - armsPosition);

        // If the B button pressed, calibrate and reset Z heading (angle theta).
//        if(gamepad2.B)  {
//            sensorGyro.calibrate();     // Calibrate gyro.
//            while (sensorGyro.isCalibrating())  {
//            }
//            sensorGyro.resetZAxisIntegrator();
//        }


        /*
         * Send telemetry data back to driver station.
         */
//        double teleCurrentPosition = 0;
//        telemetry.addData("left pwr", "left  pwr: "
//                + String.format("%.2f", leftPower));
//        telemetry.addData("right pwr", "right pwr: "
//                + String.format("%.2f", rightPower));
//        teleCurrentPosition = motorRightFront.getCurrentPosition();
//        telemetry.addData("RightMotorPosition", "RightMotorPosition:  "
//                + String.format("%.2f", teleCurrentPosition));
//        teleCurrentPosition = motorLeftFront.getCurrentPosition();
//        telemetry.addData("LeftMotorPosition", "LeftMotorPosition:  "
//                + String.format("%.2f", teleCurrentPosition));
//        telemetry.addData("ServoPosition", "actuatorServoPosition:  "
//                + String.format("%.2f", buttonSelectPosition));

        //getUSRange(10.0);
        //getGyro()
        //getLoRGB();
        //getHiRGB();
        //getTouch();

    } // loop.

    /*
     * Code to run when the op mode is exited:
     * 
     * @see com.qualcomm.robotcore.eventloop.opmode.OpMode#stop()
     */
    @Override
    public void stop() {

    } // stop


    /*
     * This method scales the joystick input via remapping so for low joystick 
     * values, the  scaled value is less than linear.  This is to make it easier 
     * to drive the robot more precisely at slower speeds.
     */
    double scaleInput(double dVal) {
        double[] scaleArray
                = {0.0, 0.05, 0.09, 0.10, 0.12, 0.15, 0.18, 0.24,
                0.30, 0.36, 0.43, 0.50, 0.60, 0.72, 0.85, 1.00, 1.00};

        // Get the corresponding index for the scaleInput array.
        int index = (int) (dVal * 16.0);
        if (index < 0) {
            index = -index;
        } else if (index > 16) {
            index = 16;
        }

        double dScale = 0.0;
        if (dVal < 0) {
            dScale = -scaleArray[index];
        } else {
            dScale = scaleArray[index];
        }

        return dScale;
    } // scaleInput


    // getUSRange
    // Ultrasonic Range Sensor: Returns boolean true = usRange > threshRange.
    // Parameter threshRange double {0-255 cm}.
    public boolean getUSRange(double threshRange) {

        double uSonicRange;      // Range value [0-255].
        boolean rangeReached = false;

        // Sample range.
        //uSonicRange = ultraSonicSensor.rawUltrasonic();   // Raw data.
//        uSonicRange = ultraSonicSensor.getDistance(DistanceUnit.CM);

//        if (uSonicRange < threshRange) {
//            rangeReached = true;
//        }

        //telemetry.addData("raw ultrasonic", uSonicRange);
//        telemetry.addData("cm", "%.2f cm", uSonicRange);
        telemetry.update();

        return rangeReached;
    }


    // getGyro
    // Returns gyro readings .
    public int getGyro() {

        int xVal, yVal, zVal;
        int thetaVal;

        // Get the x, y, and z values (rate of change of angle).
        xVal = sensorGyro.rawX();
        yVal = sensorGyro.rawY();
        zVal = sensorGyro.rawZ();

        // Get the angular rotation theta (heading) 0 - 360 deg.
        // Modern Robotics' gyro sensor keeps
        // track of the current heading for the Z axis only.
        thetaVal = sensorGyro.getHeading();
        if (thetaVal > 180) {   // Change branch cut to +- 180
            thetaVal = thetaVal - 360;
        }

        telemetry.addData("Gyro theta", String.format("%03d", thetaVal));

        return thetaVal;
    }



    // getLoLoRGB
    // Color Sensor: Returns boolean false = Unresolved, true = selectedColor.
    public boolean getLoRGB() {

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
        int getRGB = 0;

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
            getRGB = 1;
        } else {
            selectedColorFlag = false;
            getRGB = 0;
        }

        // Send information back to driver station using telemetry function.
        //telemetry.addData("Red  ", String.format("%.2f", rValue));
        //telemetry.addData("Green", String.format("%.2f", gValue));
        //telemetry.addData("Blue ", String.format("%.2f", bValue));
        telemetry.addData("Total  ", String.format("%.2f", totalValue));
        telemetry.addData("nRed  ", String.format("%.2f", nRValue));
        telemetry.addData("nGreen", String.format("%.2f", nGValue));
        telemetry.addData("nBlue ", String.format("%.2f", nBValue));
        telemetry.addData("selectedColorFlag ", selectedColorFlag);
        telemetry.update();

        return selectedColorFlag;
    }

    // getHiRGB
    // Color Sensor: Returns int 0 = Unresolved, 1 = Red, 2 = Blue.
    public int getHiRGB() {

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


    // getTouch
    // Touch Sensor: Returns boolean true = pressed switch.
    public boolean[] getTouch() {

        //Output
        boolean[] touchFlag = {false, false};
        double tppifValue;

        touchFlag[0] = false;
        touchFlag[1] = false;

        // Sample sensors.
        touchFlag[0] = touchSensor_0.isPressed();
        touchFlag[1] = touchSensor_1.isPressed();

        // Telemetry
        //telemetry.addData("Touch Value", String.valueOf(touchFlag));
        //telemetry.addData("Touch 0", String.valueOf(touchFlag[0]));
        //telemetry.addData("Touch 1", String.valueOf(touchFlag[1]));
        //telemetry.update();

        return touchFlag;
    }


} //TeleOp


