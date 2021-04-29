event_lambda_target = aws_events_targets.LambdaFunction( handler=mylambda)
        pattern={
             "source": [
             "aws.glue"
                       ],
              "detail":{
              "jobName": ["quarterdate","readcsv","readjob2"],
              "state": ["FAILED"]
                        }
                        }
        lambda_cw_event = aws_events.Rule(
            self,
            "glueRule",
            description=
            "CloudWatch event trigger for the Lambda on Glue job failure",
            event_pattern=pattern,
            enabled=True,
            targets=[event_lambda_target])
