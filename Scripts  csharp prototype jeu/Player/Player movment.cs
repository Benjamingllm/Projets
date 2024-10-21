using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.InputSystem.iOS;

public class Playermovment : MonoBehaviour
{
    [SerializeField] private float moveSpeed = 1f;
    [SerializeField] private float jumpForce = 1f;
    [SerializeField] private Vector2 mouseSens = Vector2.one;
    [SerializeField] private Transform playerCam;

    private Vector3 velocity;

    private Vector2 moveInputs,lookInputs;

    private bool jumpPerformed;

    private CharacterController characterController;



    private void Awake()
    {
        characterController = GetComponent<CharacterController>();  
    }



    private void FixedUpdate()
    {
        Vector3 horizontalVelocity = moveSpeed * new Vector3(moveInputs.x, 0,moveInputs.y);

        float _gravityVelocity = Gravity(velocity.y);

        velocity = horizontalVelocity + _gravityVelocity * Vector3.up;

        TryJump();

        Vector3 _motion = transform.right * velocity.x + transform.forward * velocity.z + transform.up * velocity.y;

        characterController.Move(_motion * Time.fixedDeltaTime);
        
    
            }

    private void TryJump()
    {
        if (!jumpPerformed || !characterController.isGrounded) return;

        velocity.y += jumpForce;
        jumpPerformed = false;
    }
    private float Gravity(float _verticalVelocity)
    {
        if (characterController.isGrounded) return 0f;

        _verticalVelocity += Physics.gravity.y * Time.fixedDeltaTime;
        return _verticalVelocity;
    }















    private void Update()
    {
        Look();
    }


    private void Look()
    {
        transform.Rotate(lookInputs.x * mouseSens.x * Time.deltaTime * Vector3.up);

        float  _camAngleX = playerCam.localEulerAngles.x - lookInputs.y * Time.deltaTime * mouseSens.y;

        if (_camAngleX <= 0f) _camAngleX = _camAngleX > 0 ? Mathf.Clamp(_camAngleX, 0f, 89.5f) : _camAngleX;
        if (_camAngleX > 270f) _camAngleX = Mathf.Clamp(_camAngleX, 270.5f, 360f); ; ;

        playerCam.localEulerAngles = Vector3.right * _camAngleX;
    }

    public void MovePerformed(InputAction.CallbackContext _ctx) => moveInputs = _ctx.ReadValue<Vector2>();

    public void LookPerformed(InputAction.CallbackContext _ctx) => lookInputs = _ctx.ReadValue<Vector2>();

    public void JumpPerformed(InputAction.CallbackContext _ctx) => jumpPerformed = _ctx.performed;

   
}
